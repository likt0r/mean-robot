import asyncio
from multiprocessing.connection import Client
import time


class BodyRunner:
    def __init__(self):
        self.value = 0

    async def run_main(self):
        while True:
            await asyncio.sleep(0.1)
            self.value += 1
