from moveit_configs_utils import MoveItConfigsBuilder
from moveit_configs_utils.launches import generate_spawn_controllers_launch


def generate_launch_description():
    moveit_config = MoveItConfigsBuilder("comau_racer5_080", package_name="comau_racer5_080_description_moveit_config").to_moveit_configs()
    return generate_spawn_controllers_launch(moveit_config)
