from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='simple_publisher_subscriber',
            executable='publisher'
        ),
        Node(
            package='simple_publisher_subscriber',
            executable='subscriber'
        ),
    ])