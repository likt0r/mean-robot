from typing import Union
from pydantic import BaseModel
from fastapi import BackgroundTasks, FastAPI
import time
import asyncio
import jsonrpclib
from body_runner import BodyRunner
app = FastAPI()

server = jsonrpclib.Server('http://localhost:9999')

runner = BodyRunner()


@app.on_event('startup')
async def app_startup():
    asyncio.create_task(runner.run_main())


@app.get("/")
async def root():
    return {"message": runner.value}


class MethodCall(BaseModel):
    path: str
    method_name: str
    param: Union[float, None] = None


@app.put("/method/")
def command(item: MethodCall):
    result = server.method(item.path, item.method_name, item.param)
    return result
