import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class HelloRoverSubscriber(Node):
    def __init__(self):
        super().__init__("hello_rover_subscriber")
        self.subscription = self.create_subscription(
            String,
            "hello_rover",
            self.listener_callback,
            10
        )
        self.get_logger().info("Hello Rover Subscriber has been started")

    def listener_callback(self, msg):
        self.get_logger().info(f"Received: '{msg.data}'")

def main():
    rclpy.init()
    node = HelloRoverSubscriber()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == "__main__":
    main()

