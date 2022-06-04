from __future__ import division
import time
import Adafruit_PCA9685
from logging import getLogger
import math
# Operating Voltage: 4.8V to 6V (Typically 5V)
# Stall Torque: 1.8 kg/cm (4.8V)
# Max Stall Torque: 2.2 kg/cm (6V)
# Operating speed is 0.1s/60° (4.8V)
# Gear Type: Metal
# Rotation : 0°-180°y
# Weight of motor : 13.4gm
logger = getLogger()

board_address = 0x40
pwm_freq = 50

pwm = Adafruit_PCA9685.PCA9685(address=board_address)

loop_freq = 10000  # 10ms in us

# board_address
# # Configure min and max servo pulse lengths
servo_min = 150  # Min pulse length out of 4096
servo_max = 600  # Max pulse length out of 4096

# Helper function to make setting a servo pulse width simpler.

PCA9685_RESOLUTION = 4096
PWM_START_MS = 0.5
PWM_STOP_MS = 2.5
PWM_FREQ = 50
PWM_STEP = 1 / PWM_FREQ / PCA9685_RESOLUTION * 1000  # step in ms

SERVO_MIN = math.ceil(PWM_START_MS / PWM_STEP)
SERVO_MAX = math.floor(PWM_STOP_MS / PWM_STEP)

print(SERVO_MIN)
print(SERVO_MAX)
# Set frequency to 60hz, good for servos.
pwm.set_pwm_freq(PWM_FREQ)  # 50 hz


def micros():
    return int((time.time())*1e6)


sleep_time = 0

logger.info("Start sensor motor loop")
while True:
    # Move servo on channel O between extremes.
    # t_start = micros()
    # pwm.set_pwm(0, 0, SERVO_MIN)

    # t_end = micros()
    # sleep_time = (loop_freq-(t_end-t_start))
    # if(sleep_time < 0):
    #     continue
    # time.sleep((loop_freq-(t_end-t_start))/1000000)

    pwm.set_pwm(0, 0, SERVO_MAX)
    time.sleep(2)
    pwm.set_pwm(0, 0, SERVO_MIN)
    time.sleep(2)
