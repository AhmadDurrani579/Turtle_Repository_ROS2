
from launch import LaunchDescription
from launch_ros.actions import Node


def generate_launch_description():
    ld = LaunchDescription()

    turtlesim_node = Node(
        
        package = "turtlesim",
        executable="turtlesim_node"
    )
    
    turtlesim_spawner_node = Node(
        
        package= "turtlesim_catch_them_all",
        executable="turtle_spawner",
        
        parameters=[
            {"spawn_frequency": 0.5},
            {"turtle_name_prefix": "my_turtle"}
        ]
     )
    
    turtle_controller_node = Node(
        package="turtlesim_catch_them_all",
        executable="turtle_controller",
        
        parameters=[
            {"catch_closet_turtle_first": True}
        ]
        
        
    )
    
    
    ld.add_action(turtlesim_node)
    ld.add_action(turtlesim_spawner_node)
    ld.add_action(turtle_controller_node)
    return ld