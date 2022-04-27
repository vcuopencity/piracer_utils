# Standard library imports
from os.path import join

from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch_ros.actions import Node
from launch_ros.actions import ComposableNodeContainer
from launch.actions import DeclareLaunchArgument
from launch_ros.descriptions import ComposableNode
from launch.conditions import IfCondition
from launch.substitutions import LaunchConfiguration


def generate_launch_description():
    camera_config = join(get_package_share_directory('piracer_utils'),
                      'cfg',  'camera.yaml')
    launch_preview = LaunchConfiguration('launch_preview')

    return LaunchDescription([
        DeclareLaunchArgument(
            'launch_preview',
            default_value='true',
            description='Determines if preview window is launched.'
        ),
        Node(
            package='v4l2_camera',
            name='v4l2_camera_node',
            executable='v4l2_camera_node',
            parameters=[camera_config],
        ),
        Node(
            package='rqt_image_view',
            name='rqt_image_view',
            executable='rqt_image_view',
            condition=IfCondition(launch_preview)
        )
    ])
