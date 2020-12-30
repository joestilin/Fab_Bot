#!/usr/bin/env python3

import board
import time
from adafruit_motorkit import MotorKit

import rospy
from geometry_msgs.msg import Twist


class MotorDriver:
    def __init__(self):
        self.motorkit = MotorKit()
        rospy.Subscriber("/cmd_vel", Twist, self.cmd_vel_callback)
        
        
    def stop(self):
        self.motorkit.motor1.throttle = 0.0
        self.motorkit.motor2.throttle = 0.0
        self.motorkit.motor3.throttle = 0.0
        self.motorkit.motor4.throttle = 0.0

    def set_throttle(self, throttle_1, throttle_2, throttle_3, throttle_4):
        if throttle >= -1.0 and throttle <= 1.0 :
            self.motorkit.motor1.throttle = throttle_1
            self.motorkit.motor2.throttle = throttle_2
            self.motorkit.motor3.throttle = throttle_3
            self.motorkit.motor4.throttle = throttle_4
        else:
            rospy.loginfo("Invalid throttle command")

    def cmd_vel_callback(self, msg):
        rospy.loginfo("Got a cmd_vel message")
        rospy.loginfo(msg)
        
        ## use msg.linear.x and msg.linear.y to generate commands to motors
        motor1 = msg.linear.x
        motor2 = 0
        motor3 = 0
        motor4 = 0
        self.set_throttle(motor_1, motor_2, motor_3, motor_4)

if __name__ == "__main__":
    rospy.init_node("motor_driver")
    rospy.loginfo("motor_driver node started")
    motor_driver = MotorDriver()
    
    rospy.on_shutdown(motor_driver.stop)
    
    rospy.spin()
            
        
        
    
    
        
        



