from fastapi import BackgroundTasks, FastAPI
import time
import asyncio
from body_runner import BodyRunner
app = FastAPI()

runner = BodyRunner()


@app.on_event('startup')
async def app_startup():
    asyncio.create_task(runner.run_main())


@app.get("/")
async def root():
    return {"message": runner.value}
