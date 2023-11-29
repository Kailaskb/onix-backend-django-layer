# subscriber.py

import rclpy
from rclpy.node import Node
from onix_backend_messages.msg import StatusData
import json

class StatusDataSubscriber(Node):
    latest_ros_data = None

    def __init__(self):
        super().__init__('status_data_subscriber')
        self.subscriber_ = self.create_subscription(StatusData, 'status_data', self.subscribe_message, 1)

    def subscribe_message(self, msg):
        self.get_logger().info('Received StatusData - mac_address: %s, time: %s, controller_voltage: %ld, total_time: %s, controller_temp: %.2f, ssid: %s, rssi: %s' %
                               (msg.mac_address, msg.time, msg.controller_voltage, msg.total_time, msg.controller_temp, msg.ssid, msg.rssi))

        self.latest_ros_data = {
            'mac_address': msg.mac_address,
            'time': msg.time,
            'controller_voltage': msg.controller_voltage,
            'total_time': msg.total_time,
            'controller_temp': msg.controller_temp,
            'ssid': msg.ssid,
            'rssi': msg.rssi
        }
        data = self.latest_ros_data
        print(f"Latest ROS data in subscribe_message: {data}")

    def get_latest_data(self):
        return self.latest_ros_data

    def get_latest_data_as_json(self):
        return json.dumps(self.latest_ros_data, indent=2)

def main(args=None):
    rclpy.init(args=args)
    status_data_subscriber = StatusDataSubscriber()
    rclpy.spin(status_data_subscriber)
    status_data_subscriber.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
