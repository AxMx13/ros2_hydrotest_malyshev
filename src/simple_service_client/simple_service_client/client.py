import sys

from string_to_num_srv.srv import CountLetters
import rclpy
from rclpy.node import Node


class MinimalClientAsync(Node):

    def __init__(self):
        super().__init__('minimal_client_async')
        self.cli = self.create_client(CountLetters, 'count_letters')
        while not self.cli.wait_for_service(timeout_sec=1.0):
            self.get_logger().info('service not available, waiting again...')
        self.req = CountLetters.Request()

    def send_request(self, a):
        self.req.input = a
        self.future = self.cli.call_async(self.req)
        rclpy.spin_until_future_complete(self, self.future)
        return self.future.result()


def main(args=None):
    rclpy.init(args=args)

    minimal_client = MinimalClientAsync()
    response = minimal_client.send_request(sys.argv[1])
    minimal_client.get_logger().info(
        f'Result of {sys.argv[1]} = {response.output}')

    minimal_client.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()