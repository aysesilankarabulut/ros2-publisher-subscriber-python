import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist


class RobotSurucu(Node):
    def __init__(self):
        super().__init__('robot_surucu')
        self.publisher_ = self.create_publisher(
            Twist, '/model/vehicle_blue/cmd_vel', 10)
        self.timer = self.create_timer(0.1, self.timer_callback)
        self.baslangic = self.get_clock().now()

    def timer_callback(self):
        gecen = (self.get_clock().now() - self.baslangic).nanoseconds / 1e9
        msg = Twist()

        if gecen < 4.0:
            msg.linear.x = 0.5      # 4 sn ileri git
        elif gecen < 7.0:
            msg.angular.z = 0.5     # 3 sn sola dön
        else:
            self.publisher_.publish(Twist())  # sıfır hız: dur
            self.get_logger().info('Rota bitti, robot durdu.')
            raise SystemExit

        self.publisher_.publish(msg)


def main(args=None):
    rclpy.init(args=args)
    node = RobotSurucu()
    try:
        rclpy.spin(node)
    except SystemExit:
        pass
    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()

