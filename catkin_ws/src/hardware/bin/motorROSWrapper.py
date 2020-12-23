#!/usr/bin/env python3

import board
import time
from adafruit_motorkit import MotorKit

import rospy
from geometry_msgs.msg import Twist

class MotorROSWrapper:
    def __init__self():
        self.motorkit = MotorKit();
        rospy.Subscriber("/cmd_vel", Twist, self.cmd_vel_callback)
        
    
    def stop(self):
        self.motorkit.motor1.throttle = 0.0
        self.motorkit.motor2.throttle = 0.0
        self.motorkit.motor3.throttle = 0.0
        self.motorkit.motor4.throttle = 0.0
    
    def set_throttle(self, throttle):
        if throttle >= -1.0 and throttle <= 1.0 :
            self.motorkit.motor1.throttle = throttle
            self.motorkit.motor2.throttle = throttle
            self.motorkit.motor3.throttle = throttle
            self.motorkit.motor4.throttle = throttle
        else:
            rospy.loginfo("Invalid throttle command")
    
    def cmd_vel_callback(msg):
        self.set_throttle(msg.linear.y);
        
            
if __name__ == "__main__":
    rospy.init_node("motor_driver")
    rospy.loginfo("motor_driver node started")
    
    motor_driver_wrapper = MotorDriverROSWrapper()
    rospy.on_shutdown(motor_driver_wrapper.stop)
    
    rospy.spin()
            
        
        
    
    
        
        



