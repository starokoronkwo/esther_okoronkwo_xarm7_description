from launch import LaunchDescription
from launch_ros.actions import Node
from launch.actions import DeclareLaunchArgument, LogInfo
from launch_ros.actions import SetParameter
from launch_ros.parameter_descriptions import ParameterValue
from launch.substitutions import Command, LaunchConfiguration
from ament_index_python.packages import get_package_share_directory
import os

def generate_launch_description():
    sim_time_parameter = SetParameter(name='use_sim_time', value=True)
    model_arg = DeclareLaunchArgument(
        name='model', default_value=os.path.join(get_package_share_directory('xarm7_description'), 'urdf', 'xarm7.urdf'), description='Abs path to urdf file'
    )
    
    robot_desc = ParameterValue(Command(['xacro ', LaunchConfiguration("model")]), value_type=str)
    robot_log = LogInfo(msg = f'robot_description: {robot_desc}')
    # urdf_file = os.path.join(
    #     get_package_share_directory('xarm7_description'),
    #     'urdf',
    #     'xarm7.urdf'
    # )

    # with open(urdf_file, 'r') as infp:
    #     robot_desc = infp.read()

    return LaunchDescription([
        sim_time_parameter,
        model_arg,
        Node(
            package='robot_state_publisher',
            executable='robot_state_publisher',
            name='robot_state_publisher',
            parameters=[{'robot_description': robot_desc}],
        ),
        Node(
            package='joint_state_publisher_gui',
            executable='joint_state_publisher_gui',
            name='joint_state_publisher_gui',
        ),
        Node(
            package='rviz2',
            executable='rviz2',
            name='rviz2',
            output='screen',
            arguments=['-d', os.path.join(get_package_share_directory('xarm7_description'), 'rviz', 'display.rviz')]
        ),
         robot_log
        
    ])
