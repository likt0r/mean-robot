import math


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
                 pwm_start_step=0

                 ):
        pwm_step = 1 / pwm_frequency / step_resolution * 1000  # step in ms
        self.id = id
        self.pwm_api = pwm_api

        self.steps_min = math.ceil(min_impulse_ms / pwm_step)
        self.steps_max = math.floor(max_impulse_ms / pwm_step)
        self.steps_center = (
            self.steps_max - self.steps_min / 2) + self.steps_min
        self.min_angle = min_angle
        self.max_angle = max_angle
        self.start_angle = start_angle
        self.pwm_frequency = 50
        self.angle_factor = (self.steps_max-self.steps_min) / \
            (max_angle-min_angle)
        self.relative_factor = (self.steps_max-self.steps_min) / 2
        # set start position
        self.current = 0
        self.pwm_api.set_pwm(self.id, 0, self.steps_min)

    def set_angle(self, angle):
        target = min(max(angle, self.min_angle),
                     self.max_angle) - self.min_angle
        self.current = round(target * self.angle_factor + self.steps_min)
        print(self.current)
        self.pwm_api.set_pwm(self.id, 0, self.current)

    def set_value(self, value):
        target = min(max(value, -1), 1)
        self.current = round(target * self.relative_factor + self.steps_min)
        self.pwm_api.set_pwm(self.id, 0, self.current)

    def center(self):
        self.current = self.steps_center
        self.pwm_api.set_pwm(self.id, 0, self.steps_center)

    def max(self):
        self.current = self.steps_max
        self.pwm_api.set_pwm(self.id, 0, self.steps_max)

    def min(self):
        self.current = self.steps_min
        self.pwm_api.set_pwm(self.id, 0, self.steps_min)
