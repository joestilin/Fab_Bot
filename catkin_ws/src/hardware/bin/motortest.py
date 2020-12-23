#!/usr/bin/env python3

import board
import time
from adafruit_motorkit import MotorKit
 
if __name__ == '__main__':
    kit = MotorKit(i2c=board.I2C())
 
    kit.motor1.throttle = 0.7
    kit.motor2.throttle = 0.7
    kit.motor3.throttle = 0.7
    kit.motor4.throttle = 0.7
    time.sleep(10.0)
    kit.motor1.throttle = -0.7
    kit.motor2.throttle = -0.7
    kit.motor3.throttle = -0.7
    kit.motor4.throttle = -0.7
    time.sleep(5.0)
    kit.motor1.throttle = 0.0
    kit.motor2.throttle = 0.0
    kit.motor3.throttle = 0.0
    kit.motor4.throttle = 0.0
