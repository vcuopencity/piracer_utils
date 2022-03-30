from launch import LaunchDescription
from launch_ros.actions import Node
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration


def generate_launch_description():
    return LaunchDescription([
        DeclareLaunchArgument(
            'agent_name',
            default_value='car1',
            description='Sets the namespace for this joy node.'),
        Node(
            package='joy',
            namespace=[LaunchConfiguration('agent_name')],
            name='joy_node',
            executable='joy_node',
        )
    ])
