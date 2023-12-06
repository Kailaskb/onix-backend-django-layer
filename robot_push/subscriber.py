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
        steer_angles_str = ', '.join(map(str, msg.steer_angles))
        r_steer_angles_str = ', '.join(map(str, msg.r_steer_angles))
        log_message = 'Received StatusData - mac_address: %s, time: %s, controller_voltage: %d, total_time: %s, controller_temp: %.2f, ssid: %s, rssi: %d, x: %f, y: %f, angle: %f, confidence: %f, current_station: %s, last_station: %s, , vx: %f, vy: %f, w: %f, steer: %f, spin: %f, r_vx: %f, r_vy: %f, r_w: %f, r_steer: %f, r_spin: %f, is_stop: %s, odo: %f, todays_odo: %f, odom_time: %d, total_run_time: %f, odom_controller_temp: %f, odom_controller_voltage: %f' % (
    msg.mac_address, msg.time, int(msg.controller_voltage), msg.total_time, msg.controller_temp, msg.ssid, int(msg.rssi), msg.x, msg.y, msg.angle, msg.confidence, msg.current_station, msg.last_station, msg.vx, msg.vy, msg.w, msg.steer, msg.spin, msg.r_vx, msg.r_vy, msg.r_w, msg.r_steer, msg.r_spin, str(msg.is_stop), msg.odo, msg.todays_odo, int(msg.odom_time), msg.total_run_time, msg.odom_controller_temp, msg.odom_controller_voltage)




        self.get_logger().info(log_message)
        
        self.latest_ros_data = {
            'mac_address': msg.mac_address,
            'time': msg.time,
            'controller_voltage': msg.controller_voltage,
            'total_time': msg.total_time,
            'controller_temp': msg.controller_temp,
            'ssid': msg.ssid,
            'rssi': msg.rssi,
            'x': msg.x,
            'y' : msg.y,
            'angle' : msg.angle,
            'confidence' : msg.confidence,
            'current_station' : msg.current_station,
            'last_station' : msg.last_station,
            'vx' : msg.vx,
            'vy' : msg.vy,
            'w' : msg.w,
            'steer' : msg.steer,
            'spin' : msg.spin,
            'r_vx' : msg.r_vx,
            'r_vy' : msg.r_vy,
            'r_w' : msg.r_w,
            'r_steer' : msg.r_steer,
            'r_spin' : msg.r_spin,
            'steer_angles' : msg.steer_angles,
            'r_steer_angles' : msg.r_steer_angles,
            'is_stop' : msg.is_stop,
            'odo' : msg.odo,
            'todays_odo' : msg.todays_odo,
            'odom_time' : msg.odom_time,
            'total_run_time' : msg.total_run_time,
            'odom_controller_temp' : msg.odom_controller_temp,
            'odom_controller_voltage' : msg.odom_controller_voltage
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
