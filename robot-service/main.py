import time
import threading

from control_loop import create_loop as create_control_loop
from server import create_loop as create_server_loop
# from socket import socket_listener
from store import ThreadSafeStore
import threading
import queue
method_queue = queue.Queue()
# method_queue item ["path", "method_name", param_1, ..., param_n]
# init store
store = ThreadSafeStore(
    config_filepath='/home/pi/mean-robot/robot-service/store_init.yaml')


# Created the Threads
control_loop = threading.Thread(target=create_control_loop(method_queue))
server = threading.Thread(target=create_server_loop(method_queue))

# Started the threads
control_loop.start()
server.start()

# Joined the threads
control_loop.join()
server.join()
