#!/usr/bin/env python3
import rclpy
from rclpy.node import Node

from my_robot_interfaces.msg import Ledstates
from my_robot_interfaces.srv import Setled

class LedManagerNode(Node):  # MODIFY NAME
    def __init__(self):
        super().__init__("led_panel")  # MODIFY NAME

        # Declare and retrieve parameter
        self.declare_parameter("led_states", [0, 0, 0])
        raw_led_states = self.get_parameter("led_states").value

        # Ensure the parameter is a valid sequence of integers
        if not isinstance(raw_led_states, list) or not all(isinstance(i, int) for i in raw_led_states):
            self.get_logger().error("Parameter 'led_states' must be a list of integers. Using default value [0, 0, 0].")
            self.led_states = [0, 0, 0]
        else:
            self.led_states = raw_led_states

        self.led_states_publisher = self.create_publisher(Ledstates, "led_states", 10)
        self.led_states_timer = self.create_timer(4, self.publish_led_states)

        self.set_led_service_ = self.create_service(Setled, "set_led", self.callback_set_led)
        self.get_logger().info("Led Node has been started")

    def publish_led_states(self):
        msg = Ledstates()
        msg.led_states = self.led_states
        self.led_states_publisher.publish(msg)

    def callback_set_led(self, request, response):
        led_number = request.led_number
        state = request.state

        if led_number > len(self.led_states) or led_number <= 0:
            response.success = False
            return response

        if state not in [0, 1]:
            response.success = False
            return response

        self.led_states[led_number - 1] = state
        response.success = True

        return response


def main(args=None):
    rclpy.init(args=args)
    node = LedManagerNode()  # MODIFY NAME
    rclpy.spin(node)
    rclpy.shutdown()


if __name__ == "__main__":
    main()
