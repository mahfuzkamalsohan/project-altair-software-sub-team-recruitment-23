import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
import cv2

class VideoPublisher(Node):
    def __init__(self):
        super().__init__('video_publisher')
        self.publisher_ = self.create_publisher(Image, '/camera/image_raw', 10)
        self.br = CvBridge()
        
        self.cap = cv2.VideoCapture(0) # 0 = default webcam

        # Timer callback at 30 FPS
        self.timer = self.create_timer(1/30, self.timer_callback)

    def timer_callback(self):
        ret, frame = self.cap.read()
        if ret:
            # Convert OpenCV image (BGR) to ROS Image message
            msg = self.br.cv2_to_imgmsg(frame, encoding='bgr8')
            self.publisher_.publish(msg)
            self.get_logger().info('Publishing video frame')
        else:
            self.get_logger().warn('Failed to capture frame')

    def destroy_node(self):
        self.cap.release()
        super().destroy_node()

def main(args=None):
    rclpy.init(args=args)
    node = VideoPublisher()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()