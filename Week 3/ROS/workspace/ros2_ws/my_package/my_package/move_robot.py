import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
import time

class MoveRobot(Node):
    def __init__(self):
        super().__init__('move_robot')
        self.pub = self.create_publisher(Twist, '/cmd_vel', 10)
        self.move_sequence()

    def move_sequence(self):
        # Move forward 3s
        self.publish_velocity(0.5, 0.0, 3.0)
        # Rotate in place 2s
        self.publish_velocity(0.0, 0.5, 2.0)
        # Move forward again 3s
        self.publish_velocity(0.5, 0.0, 3.0)

    def publish_velocity(self, linear_x, angular_z, duration):
        start = self.get_clock().now()
        while (self.get_clock().now() - start).nanoseconds / 1e9 < duration:
            msg = Twist()
            msg.linear.x = linear_x
            msg.angular.z = angular_z
            self.pub.publish(msg)
            time.sleep(0.1)

        # Stop
        msg = Twist()
        msg.linear.x = 0.0
        msg.angular.z = 0.0
        self.pub.publish(msg)

def main():
    rclpy.init()
    node = MoveRobot()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()

