import threading
import logging
import yaml


class ThreadSafeStore:
    _instance = None
    _initialized = False
    _lock = threading.Lock()

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            with cls._lock:
                # another thread could have created the instance
                # before we acquired the lock. So check that the
                # instance is still nonexistent.
                if not cls._instance:
                    cls._instance = super(ThreadSafeStore, cls).__new__(cls)
        return cls._instance

    def __init__(self):
        """Initialize the instance"""
        if self._initialized is False:
            with open('robot-service/store.yaml', 'r') as file:
                self._map = yaml.safe_load(file)
                self._logger = logging.getLogger(self.__class__.__name__)
                self._initialized = True

        self._logger.debug("using instance: %s" % self._instance)

    def set(self, path, value):
        """set a value"""
        result = self._map
        parts = path.split('.')
        for part in parts[:-1]:
            result = result[part]
        result[parts[-1]] = value
        self._logger.debug("set {} {}".format(path, value))

    def get(self, path):
        """get a value"""
        result = self._map
        parts = path.split('.')
        for part in parts:
            result = result[part]

        self._logger.debug("get {} : {}".format(path, result))
        return result
