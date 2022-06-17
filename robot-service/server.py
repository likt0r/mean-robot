from jsonrpclib.SimpleJSONRPCServer import SimpleJSONRPCServer
from store import ThreadSafeStore
import logging
import time
from servo import methods_dict


def create_loop(methods_queue):
    def loop():
        store = ThreadSafeStore()
        time.sleep(4)  # wait till sensor loop is initialized

        def get(path):
            return store.get(path)

        def set(path, value):
            return store.set(path, value)

        def method(path, method_name, value):
            if (method_name in methods_dict.keys()):
                return methods_queue.put([path, method_name, value])
            return False

        server = SimpleJSONRPCServer(('localhost', 9999), logRequests=False)
        server.register_function(get)
        server.register_function(set)
        server.register_function(method)
        server.serve_forever()
    return loop
