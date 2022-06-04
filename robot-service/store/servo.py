
def get_servo_dict(key, id, speed, pulse_min, pulse_max, angle_min, angle_max, angle_start, step_resolution, angle_max_velocity):
    return {
        "key": key,
        "id": id,
        "type": "servo",
        "speed": speed,
        "pulse_min": pulse_min,
        "pulse_max": pulse_max,
        "angle_min": angle_min,
        "angle_max": angle_max,
        "angle_start": angle_start,
        "angle_target": 0,
        "angle_current": 0,
        "relative_target": 0,
        "relative_current": 0,
        "step_target": 0,
        "step_current": 0,
        "step_resolution": step_resolution,
        "angle_max_velocity": angle_max_velocity,
    }
