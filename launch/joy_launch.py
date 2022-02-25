from launch import LaunchDescription
from launch_ros.actions import Node


def generate_launch_description():
    ld = LaunchDescription()

    joy_node = Node(
        package='joy',
        namespace='car1',
        name='joy_node',
        executable='joy_node',
    )

    ld.add_action(joy_node)

    return ld
