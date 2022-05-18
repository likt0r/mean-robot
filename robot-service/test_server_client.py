from cmath import sin
import jsonrpclib
import math
from time import sleep
server = jsonrpclib.Server('http://localhost:9999')
# print(server.echo("hallo"))
# server.set("actuators.head_yaw.target_position", 0.5)
# print(server.get("actuators.head_yaw.target_position"))
x = 0
server.set("actuators.m11.target_position", -0.03)
server.set("actuators.m21.target_position", -0.03)
server.set("actuators.m31.target_position", -0.03)
server.set("actuators.m12.target_position", -0.03)
server.set("actuators.m22.target_position", -0.03)
server.set("actuators.m32.target_position", -0.03)
sleep(2)
phase_shift = math.pi / 2
step = 0
while True:
    if step == 0:
        server.set("actuators.m31.target_position",
                   -1*(max(0, math.sin(math.pi * x)) + 0.03))
        server.set("actuators.m21.target_position",
                   -1*(max(0, math.sin(math.pi * (x+0.1))) + 0.03))
        server.set("actuators.m11.target_position",
                   -1*(max(0, math.sin(math.pi * (x+0.2))) + 0.03))
        server.set("actuators.m32.target_position",
                   -1*(max(0, math.sin(math.pi * (x+phase_shift))) + 0.03))
        server.set("actuators.m22.target_position",
                   -1*(max(0, math.sin(math.pi * (x+0.1+phase_shift))) + 0.03))
        server.set("actuators.m12.target_position",
                   -1*(max(0, math.sin(math.pi * (x+0.2+phase_shift))) + 0.03))
        x = x + 0.04
        if(x > 15):
            step = step + 1
            x = 0
    if step == 1:
        server.set("actuators.m11.target_position", -0.03)
        server.set("actuators.m21.target_position", -0.03)
        server.set("actuators.m31.target_position", -0.03)
        server.set("actuators.m12.target_position", -0.03)
        server.set("actuators.m22.target_position", -0.03)
        server.set("actuators.m32.target_position", -0.03)
        sleep(2)
        step = step + 1
    if step == 2:
        server.set("actuators.m21.target_position", -1)
        sleep(1)
        server.set("actuators.m21.target_position", -0.03)
        server.set("actuators.m32.target_position", -1)
        sleep(1)
        server.set("actuators.m21.target_position", -0.03)
        server.set("actuators.m32.target_position", -0.03)
        sleep(1)
        server.set("actuators.m11.target_position", -1)
        server.set("actuators.m22.target_position", -1)
        sleep(1)
        server.set("actuators.m11.target_position", -0.03)
        server.set("actuators.m22.target_position", -0.03)
        server.set("actuators.m31.target_position", -1)
        server.set("actuators.m12.target_position", -1)
        sleep(1)
        server.set("actuators.m31.target_position", -0.03)
        server.set("actuators.m12.target_position", -0.03)
        sleep(1)
        step = 0
    sleep(0.01)
