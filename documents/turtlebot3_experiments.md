# Turtlesim3 Experiments

## Launch Simulation World

### Empty World
```
$ roslaunch turtlebot3_gazebo turtlebot3_empty_world.launch
```

### TurtleBot3 World
```
$ roslaunch turtlebot3_gazebo turtlebot3_world.launch
```

### TurtleBot3 House
```
$ roslaunch turtlebot3_gazebo turtlebot3_house.launch
```

## Teleoperation 
In order to teleoperate the TurtleBot3 with the keyboard, launch the teleoperation node with below command in a new terminal window.
```
$ roslaunch turtlebot3_teleop turtlebot3_teleop_key.launch
```

##  Run a SLAM Node

Open a new terminal from Remote PC with `Ctrl + Alt + T` and run the SLAM node. `Gmapping SLAM` method is used by default.
Please use the proper keyword among `burger`, `waffle`, `waffle_pi` for the `TURTLEBOT3_MODEL` parameter.

```
$ roslaunch turtlebot3_slam turtlebot3_slam.launch slam_methods:=gmapping
```

## Save Map
When the map is created successfully, open a new terminal from Remote PC with `Ctrl + Alt + T` and save the map.

```
$ rosrun map_server map_saver -f ~/map
```

## Run Navigation Node
Open a new terminal from Remote PC with `Ctrl + Alt + T` and run the Navigation node.

```
$ roslaunch turtlebot3_navigation turtlebot3_navigation.launch map_file:=$HOME/map.yaml
```
# Reference
[1] [Turtlebot3 Simulation Experiments](https://emanual.robotis.com/docs/en/platform/turtlebot3/simulation/)
