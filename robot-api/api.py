from fastapi import FastAPI
import time
app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


async def control_loop():
    while True:
        # Move servo on channel O between
        print(0)
        time.sleep(1)
        #pwm.set_pwm(1, 0, servo_min)
        print(1)
        time.sleep(1)

print("Start Control loop")
control_loop()
