from launch import LaunchDescription
from launch_ros.actions import Node
from launch.actions import ExecuteProcess

def generate_launch_description():
    return LaunchDescription([
        # Command to play the ROS 2 bag
        ExecuteProcess(
            cmd=['ros2', 'bag', 'play', '/mnt/data/bag_db/slam_gnss_lidar_1/', '--clock'],
            output='screen'
        ),
        # Command to run the robot_state_publisher
        Node(
            package='robot_state_publisher',
            executable='robot_state_publisher',
            name='robot_state_publisher',
            arguments=['/mnt/data/bag_db/slam_gnss_lidar_1/configs/urdf/peter.urdf'],
            parameters=[{'use_sim_time': True, 'cache_time': 10.0}],
            output='screen'
        )
    ])