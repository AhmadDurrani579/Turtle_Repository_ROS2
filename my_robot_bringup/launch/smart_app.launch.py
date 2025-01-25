
from launch import LaunchDescription
from launch_ros.actions import Node


def generate_launch_description():
    ld = LaunchDescription()
    
    robot_names = ["Giskard", "BBB", "Daneel", "Jander", "CSP30"]
    
    robot_news_station_nodes = []
    
    for name in robot_names:
       robot_news_station_nodes.append(Node(
        package= "my_py_pkg",
        executable= "robot_news_station",
        name="robot_news_station" + name.lower(),
        parameters=[
            {"robot_name": name}
        ]
      ))    
    
    smartphone = Node(
       package= "my_py_pkg",
       executable= "smartphone",
       name= "robot_news_smartphone_giskard"
        
    )   
    
    for node in robot_news_station_nodes:
        ld.add_action(node)
        
    ld.add_action(smartphone)
    return ld