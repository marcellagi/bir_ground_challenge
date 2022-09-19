#!/usr/bin/env python3

import rospy
from std_msgs.msg import Bool
import detect_parking as dp

class State:
  
    def __init__(self):
       
        self.pose_publisher1 = rospy.Publisher('/detect_tunnel',Bool,queue_size=10)
        self.pose_publisher2= rospy.Publisher('/detect_parking',Bool,queue_size=10)
        self.pose_publisher3 = rospy.Publisher('/detect_construction',Bool,queue_size=10)
        self.pose_publisher4 = rospy.Publisher('/make_da_mission',Bool,queue_size=10)


    def parking(self): 
        a = Bool()
        a.data = True
        self.pose_publisher1.publish(a)
    

if __name__ == '__main__':
    rospy.init_node("state_manager", anonymous=True)  #cria o nó 
    bebe = State()
    while (True):
      p = dp.DetectParking()
      
      bebe.parking()
      