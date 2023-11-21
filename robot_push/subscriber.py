# subscriber.py

import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
import json

class MinimalSubscriber(Node):
    latest_ros_data = None

    def __init__(self):
        super().__init__('py_sub_spiral_node')
        self.subscriber_ = self.create_subscription(Twist, 'turtle1/cmd_vel', self.subscribe_message, 1)

    def subscribe_message(self, msg):
        self.get_logger().info('Received - Linear Velocity: %f, Angular Velocity: %f' % (msg.linear.x, msg.angular.z))
        self.latest_ros_data = {'linear': msg.linear.x, 'angular': msg.angular.z}
        data = self.latest_ros_data
        print(f"Latest ROS data in subscribe_message: {data}")

    def get_latest_data(self):
        return self.latest_ros_data

    def get_latest_data_as_json(self):
        return json.dumps(self.latest_ros_data, indent=2)

def main(args=None):
    rclpy.init(args=args)
    minimal_subscriber = MinimalSubscriber()
    rclpy.spin(minimal_subscriber)
    minimal_subscriber.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()