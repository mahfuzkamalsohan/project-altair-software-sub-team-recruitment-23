import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
import math
import time

class MoveTurtle(Node):
    def __init__(self):
        super().__init__('move_turtle')
        self.publisher = self.create_publisher(Twist, '/turtle1/cmd_vel', 10)

        # Ask user to choose movement type
        command = input("Enter command: A (circle), B (square), C (spiral): ").upper()

        if command == "A":
            self.move_circle()  # Circle: constant forward + rotation
        elif command == "B":
            self.move_square()  # Square: move straight + turn 90° four times
        elif command == "C":
            self.move_spiral()  # Spiral: gradually increase forward speed while rotating
        else:
            print("Invalid input. Exiting.")

    def publish_velocity(self, linear_x, angular_z, duration):
        start = self.get_clock().now()
        while (self.get_clock().now() - start).nanoseconds / 1e9 < duration:
            msg = Twist()
            msg.linear.x = linear_x
            msg.angular.z = angular_z
            self.publisher.publish(msg)
            time.sleep(0.1)

        # Stop turtle after movement
        msg = Twist()
        msg.linear.x = 0.0
        msg.angular.z = 0.0
        self.publisher.publish(msg)

    def move_circle(self):
        # Circle: forward + rotation simultaneously
        # linear.x = 2.0  forward speed
        # angular.z = 2.0  rotation speed
        self.publish_velocity(2.0, 2.0, 5.0)

    def move_square(self):
        # Square: repeat 4 times -> move straight, then turn 90 degrees
        # linear.x = 2.0  straight line speed
        # angular.z = pi/2  turn 90 degrees
        for _ in range(4):
            self.publish_velocity(2.0, 0.0, 2.0)        # Move straight
            self.publish_velocity(0.0, math.pi/2, 1.0) # Turn 90 degrees

    def move_spiral(self):
        # Spiral: gradually increase forward speed while rotating
        linear = 0.5   # initial forward speed, slower than circle to make the spiral gradual
        angular = 2.0  # rotation speed, higher than forward
        duration = 10
        step = 0.1
        start = self.get_clock().now()

        while (self.get_clock().now() - start).nanoseconds / 1e9 < duration:
            msg = Twist()
            msg.linear.x = linear
            msg.angular.z = angular
            self.publisher.publish(msg)
            linear += 0.05  # gradually increase forward speed to make spiral expand outward
            time.sleep(step)

        # Stop turtle after spiral
        msg = Twist()
        msg.linear.x = 0.0
        msg.angular.z = 0.0
        self.publisher.publish(msg)


def main(args=None):
    rclpy.init(args=args)
    node = MoveTurtle()
    node.destroy_node()
    rclpy.shutdown()


if __name__ == "__main__":
    main()

