import time
import threading

from control_loop import loop
from server import loop as server_loop
# from socket import socket_listener
from store import ThreadSafeStore

# init store
store = ThreadSafeStore(
    config_filepath='/home/pi/mean-robot/robot-service/store_init.yaml')


# Created the Threads
control_loop = threading.Thread(target=loop)
server = threading.Thread(target=server_loop)

# Started the threads
control_loop.start()
server.start()

# Joined the threads
control_loop.join()
server.join()
