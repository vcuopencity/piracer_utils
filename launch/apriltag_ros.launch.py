# Standard library imports
from os.path import join

import launch
from ament_index_python.packages import get_package_share_directory
from launch_ros.actions import ComposableNodeContainer
from launch_ros.descriptions import ComposableNode


def generate_launch_description():
    car_config = join(get_package_share_directory('piracer_utils'),
                      'cfg',  'apriltag_ros', 'opencity.yaml')
    composable_node = ComposableNode(
        name='apriltag',
        package='apriltag_ros', plugin='AprilTagNode',
        remappings=[("/apriltag/image", "/image_raw"), ("/apriltag/camera_info", "/camera_info")],
        parameters=[car_config])
    container = ComposableNodeContainer(
        name='tag_container',
        namespace='apriltag',
        package='rclcpp_components',
        executable='component_container',
        composable_node_descriptions=[composable_node],
        output='screen'
    )

    return launch.LaunchDescription([container])