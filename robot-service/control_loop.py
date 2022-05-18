from __future__ import division
import time
import Adafruit_PCA9685
from store import ThreadSafeStore
from logging import getLogger

logger = getLogger()

board_address = 0x40
pwm_freq = 50

pwm = Adafruit_PCA9685.PCA9685(address=board_address)
pwm.set_pwm_freq(pwm_freq)
loop_freq = 10000  # 10ms in us

# board_address
# # Configure min and max servo pulse lengths
servo_min = 150  # Min pulse length out of 4096
servo_max = 600  # Max pulse length out of 4096

# Helper function to make setting a servo pulse width simpler.
store = ThreadSafeStore()

# Set frequency to 60hz, good for servos.
pwm.set_pwm_freq(60)


def micros():
    return int((time.time())*1e6)


sleep_time = 0


def loop():
    logger.info("Start sensor motor loop")
    while True:
        # Move servo on channel O between extremes.
        t_start = micros()
        # do actuators
        actuators = store.get("actuators")
        for key, value in actuators.items():
            target = int(((value["target_position"]+1)/2) *
                         (value["pulse_max"]-value["pulse_min"]) + value["pulse_min"])
            pwm.set_pwm(value["id"], 0, target)

        # do sensors
        sensors = store.get("sensors")
        t_end = micros()
        sleep_time = (loop_freq-(t_end-t_start))
        if(sleep_time < 0):
            # loop to long don't sleep
            # logger.warn("Missed Frame by {}".format(sleep_time/1000000))
            continue
        time.sleep((loop_freq-(t_end-t_start))/1000000)
