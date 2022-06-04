from jsonrpclib.SimpleJSONRPCServer import SimpleJSONRPCServer
from store import ThreadSafeStore
import logging
import time


def loop():
    store = ThreadSafeStore()
    time.sleep(4)  # wait till sensor loop is initialized

    def get(path):
        return store.get(path)

    def set(path, value):
        return store.set(path, value)
    server = SimpleJSONRPCServer(('localhost', 9999), logRequests=False)
    server.register_function(get)
    server.register_function(set)
    server.register_function(lambda x: x, 'echo')
    server.serve_forever()
