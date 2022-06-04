import threading
import logging
import yaml
from store.servo import get_servo_dict


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

    def __init__(self, config_filepath=None):
        """Initialize the instance"""
        if self._initialized is False and config_filepath is not None:
            with open(config_filepath, 'r') as file:
                init_dict = yaml.safe_load(file)
                self._map = {"actuators": {}}
                for key, value in init_dict["actuators"].items():
                    self._map["actuators"][key] = get_servo_dict(
                        key,
                        value["id"],
                        value["speed"],
                        value["pulse_min"],
                        value["pulse_max"],
                        value["angle_min"],
                        value["angle_max"],
                        value["angle_start"],
                        value["step_resolution"],
                        value["angle_max_velocity"])
                self._logger = logging.getLogger(self.__class__.__name__)
                self._initialized = True
                print(self._map)
        self._logger.debug("using instance: %s" % self._instance)

    def set(self, path, value):
        """set a value"""
        with self._lock:
            result = self._map
            parts = path.split('.')
            for part in parts[:-1]:
                result = result[part]
            result[parts[-1]] = value
            self._logger.debug("set {} {}".format(path, value))

    def get(self, path):
        """get a value"""
        with self._lock:
            result = self._map
            parts = path.split('.')
            for part in parts:
                result = result[part]

            self._logger.debug("get {} : {}".format(path, result))
            return result
