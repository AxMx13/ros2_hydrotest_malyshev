from string_to_num_srv.srv import CountLetters

import rclpy
from rclpy.node import Node


class MinimalService(Node):

    def __init__(self):
        super().__init__('minimal_service')
        self.srv = self.create_service(CountLetters, 'count_letters', self.count_letters_callback)

    def count_letters_callback(self, request, response):
        response.output = len(request.input)
        self.get_logger().info(f'Incoming request: {request.input}')

        return response


def main(args=None):
    rclpy.init(args=args)

    minimal_service = MinimalService()

    rclpy.spin(minimal_service)

    rclpy.shutdown()


if __name__ == '__main__':
    main()