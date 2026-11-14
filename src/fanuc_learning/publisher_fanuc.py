### make this node to test launch ##
#version 1.0
#date 2026/11/13
###################################
import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class FanucPublisher(Node):  
    def __init__(self):
        super().__init__('fanuc_publisher')
        self.publisher_ = self.create_publisher(String, 'fanuc_topic', 10)
        timer_period = 1.0  # seconds
        self.timer = self.create_timer(timer_period, self.timer_callback)
        self.i = 10 # modify from 1 to 10

    def timer_callback(self):
        msg = String()
        msg.data = f'Hello Fanuc {self.i}'
        self.publisher_.publish(msg)
        self.get_logger().info(f'Publishing: "{msg.data}"')
        self.i += 1


def main(args=None):  
    rclpy.init(args=args)
    fanuc_publisher = FanucPublisher()
    
    

    try:
        rclpy.spin(fanuc_publisher)
    except KeyboardInterrupt:
        pass    
    finally:
        fanuc_publisher.destroy_node()
        rclpy.shutdown()    


if __name__ == '__main__':  
    main()                     
