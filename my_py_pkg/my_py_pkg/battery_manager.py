#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
 

class BatteryManagerNode(Node): # MODIFY NAME
    def __init__(self):
        super().__init__("battery_status_manager") # MODIFY NAME
 
 
def main(args=None):
    rclpy.init(args=args)
    node = BatteryManagerNode() # MODIFY NAME
    rclpy.spin(node)
    rclpy.shutdown()
 
 
if __name__ == "__main__":
    main()
    
    