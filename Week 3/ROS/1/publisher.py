import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class HelloRoverPublisher(Node):
    def __init__(self):
        super().__init__("hello_rover_publisher")

        self.publisher = self.create_publisher(String, "hello_rover", 10)
        timer_period = 1.0
        self.timer = self.create_timer(timer_period, self.timer_callback)

        self.get_logger().info("Hello Rover Publisher has been started")

    def timer_callback(self):
        msg = String()
        msg.data = "Hello Rover"
        self.publisher.publish(msg)
        #self.get_logger().info(f"Publishing: '{msg.data}'")

def main(args=None):
    rclpy.init(args=args)
    node = HelloRoverPublisher()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == "__main__":
    main()