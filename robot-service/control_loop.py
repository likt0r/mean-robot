from __future__ import division
import time
import Adafruit_PCA9685
from store import ThreadSafeStore
from logging import getLogger
from servo import Servo

# Set frequency to 60hz, good for servos.
PWM_FREQUENCY = 60
LOOP_FREQUENCY = 80
logger = getLogger()

board_address = 0x40


pwm = Adafruit_PCA9685.PCA9685(address=board_address)
pwm.set_pwm_freq(PWM_FREQUENCY)
loop_freq = 1/LOOP_FREQUENCY*1000000  # 10ms in us

# board_address
# # Configure min and max servo pulse lengths
servo_min = 150  # Min pulse length out of 4096
servo_max = 600  # Max pulse length out of 4096

# Helper function to make setting a servo pulse width simpler.


def micros():
    return int((time.time())*1e6)


sleep_time = 0


def loop():
    actuators = []
    store = ThreadSafeStore()
    info = store.get("actuators")
    logger.info("Initialize actuators")
    for key, value in info.items():
        actuators.append((key, Servo(value["id"],
                                     pwm,
                                     pulse_min=value["pulse_min"],
                                     pulse_max=value["pulse_max"],
                                     angle_min=value["angle_min"],
                                     angle_start=value["angle_start"],
                                     angle_max=value["angle_max"],
                                     step_resolution=value["step_resolution"],
                                     angle_max_velocity=value["angle_max_velocity"],
                                     pwm_frequency=PWM_FREQUENCY,
                                     loop_frequency=LOOP_FREQUENCY,
                                     )))

    logger.info("Start sensor motor loop")

    while True:
        # Move servo on channel O between extremes.
        t_start = micros()
        # do actuators

        for (key, servo) in actuators:
            servo.loop()
        # for i in range(0, 15):
        #     pwm.set_pwm(i, 0, 300)
        # do sensors
        # sensors = store.get("sensors")
        t_end = micros()
        sleep_time = (loop_freq-(t_end-t_start))
        if(sleep_time < 0):
            # loop to long don't sleep
            logger.warn("Missed Frame by {}".format(sleep_time/1000000))
            continue
        time.sleep((loop_freq-(t_end-t_start))/1000000)
