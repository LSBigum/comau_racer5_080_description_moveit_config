import os
from moveit_configs_utils import MoveItConfigsBuilder
from moveit_configs_utils.launches import generate_demo_launch
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    # moveit_config = (
    #     MoveItConfigsBuilder("moveit_resources_fanuc")
    #     .robot_description(file_path="config/fanuc.urdf.xacro")
    #     .robot_description_semantic(file_path="config/fanuc.srdf")
    #     .trajectory_execution(file_path="config/moveit_controllers.yaml")
    #     .to_moveit_configs()
    # )
        
    
    moveit_config = (
        MoveItConfigsBuilder("comau_racer5_080_description")
        .robot_description(file_path="config/comau_racer5_080.urdf.xacro")
        .robot_description_semantic(file_path="config/comau_racer5_080.srdf")
        .trajectory_execution(file_path="config/moveit_controllers.yaml")
        .to_moveit_configs()
    )
    
    ros2_controllers_path = os.path.join(
        get_package_share_directory("comau_racer5_080_description_moveit_config"),
        "config",
        "ros2_controllers.yaml",
    )

    ros2_control_node = Node(
        package="controller_manager",
        executable="ros2_control_node",
        parameters=[moveit_config.robot_description, ros2_controllers_path],
        output="both",
    )
    
    fanuc_controller_spawner = Node(
        package="controller_manager",
        executable="spawner",
        arguments=[
            "comau_racer5_080_controller",
            "--controller-manager",
            "/controller_manager",
        ],
    )
        
    return LaunchDescription([ros2_control_node])