import math


def sign(x):
    if x > 0:
        return 1
    elif x == 0:
        return 0
    else:
        return -1


class Servo:
    def __init__(self,
                 id,
                 pwm_api,
                 min_impulse_ms=1,
                 max_impulse_ms=2,
                 min_angle=0,
                 start_angle=45,
                 max_angle=90,
                 pwm_frequency=50,
                 step_resolution=4096,  # 12bit
                 max_angle_velocity=600,  # 600° per second
                 loop_frequency=100,
                 ):
        pwm_step = 1 / pwm_frequency / step_resolution * 1000  # step in ms
        self.id = id
        self.pwm_api = pwm_api

        self.steps_min = math.ceil(min_impulse_ms / pwm_step)
        self.steps_max = math.floor(max_impulse_ms / pwm_step)
        self.steps_center = round(
            self.steps_max - self.steps_min / 2) + self.steps_min
        self.min_angle = min_angle
        self.max_angle = max_angle
        self.start_angle = start_angle
        self.pwm_frequency = 50
        self.angle_factor = (self.steps_max-self.steps_min) / \
            (max_angle-min_angle)

        self.relative_factor = (self.steps_max-self.steps_min) / 2
        self.steps_start = round(start_angle * self.angle_factor)

        self.max_steps_change = round(
            max_angle_velocity/loop_frequency * self.angle_factor)
        # set start position
        self.current = self.steps_min
        self.pwm_api.set_pwm(self.id, 0, self.steps_start)

    def set_velocity(self, velocity):
        self.current_loop_change = min(
            max(velocity, 0), 1) * self.max_steps_change
        print('Current velocity {}, {}'.format(
            velocity, self.current_loop_change))

    def set_angle(self, angle):
        tmp = min(max(angle, self.min_angle),
                  self.max_angle) - self.min_angle
        self.target = round(tmp * self.angle_factor + self.steps_min)
        print(self.target)
        #self.pwm_api.set_pwm(self.id, 0, self.current)

    def set_value(self, value):
        tmp = min(max(value, -1), 1)
        self.target = round(tmp * self.relative_factor + self.steps_min)
        print(self.target)
        # .pwm_api.set_pwm(self.id, 0, self.current)

    def center(self):
        self.target = self.steps_center
        # self.pwm_api.set_pwm(self.id, 0, self.steps_center)

    def max(self):
        self.target = self.steps_max
        # self.pwm_api.set_pwm(self.id, 0, self.steps_max)

    def min(self):
        self.target = self.steps_min
        # self.pwm_api.set_pwm(self.id, 0, self.steps_min)

    def loop(self):
        # print("Before current {}  vs  target {}  vel {}".format(
        #     self.current, self.target, self.current_loop_change))
        self.current = self.current + \
            sign(self.target-self.current) * \
            (min(abs(self.target-self.current), self.current_loop_change))
        # print("After current {}  vs  target {}".format(self.current, self.target))
        self.pwm_api.set_pwm(self.id, 0, round(self.current))

    def get_store_dict(): 
        return {
            
        }
    