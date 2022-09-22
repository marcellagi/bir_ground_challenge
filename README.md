# bir_ground_challenge

![figure](./source/turtle-map.png)

This repository supports the development of the ground robotics challenge from [RASC](https://www.braziliansinrobotics.com/).

**Keywords**: Challenge, Ground-robotics, Turtlebot3


**Sharp your spear!**

_For a good development it is suggested that you perform the following tutorials_

- [ROS2](https://docs.ros.org/en/foxy/Tutorials.html)
- [turtlebot3](https://emanual.robotis.com/docs/en/platform/turtlebot3/overview/)
- [Nav2](https://navigation.ros.org/)

## Justification

Developing skills and knowledge in navigation is very important for a researcher in the field of robotics, in view of the growth of mobile robotics applied to the theme "robots in terrestrial environment", it is necessary to develop mechanisms that solidify knowledge in a practical way. Concepts such as *SLAM, State-machine, computer vision and localization* are quite recurrent in this context, so, the **Heavy Hull** challenge proposes the systematic application of these concepts in order to strengthen future developments.

## Objective

The objective is to carry out the [mission](#heavy-hull-mission) obeying the [prerequisites](#prerequisites).


## Heavy Hull Mission

The [**Turtlebot 3**](https://emanual.robotis.com/docs/en/platform/turtlebot3/overview/) must go through a delimited [environment](#Environment) starting at the start point highlighted in the [example environment](#example-environment), being positioned with the camera facing away from the entrance. The mission environment is similar to a maze, composed of two corridors and with the 3 previously placed [fiducial markers](#aruco-fiducial-marker). The robot must go through the environment completely and reach the end point, at the end of the route (arrival at the final point) there will be an [object](#object) that must be identified.

### Environment

#### Example environment

![figure](./source/envedited.png)

### Object

The object to be identified is an orange ball

<img src="./source/ball.jpg" alt="drawing" width="300"/>

### ArUco fiducial marker

The markers used must be of the ArUco type

<img src="./source/aruco.png" alt="drawing" width="400"/>

## Prerequisites

- The challenge must be performed using [ROS2](https://docs.ros.org/en/foxy/index.html)
- For autonomous navigation, ***state-machine*** must be used
- The simulation and real [environment](#environment) must be built based on the [example environment](#example-environment)
- The [**Turtlebot 3**](https://emanual.robotis.com/docs/en/platform/turtlebot3/overview/) must make the [environment](#environment) map while executing the [mission](#heavy-hull-mission)
- The [**Turtlebot 3**](https://emanual.robotis.com/docs/en/platform/turtlebot3/overview/) must use **three** [fiducial markers](#aruco-fiducial-marker) for localization

## Any Questions?


[Anderson Lima](https://github.com/aldenpower) : _eng.andersonfsl@gmail.com_
[Marco Reis](https://github.com/mhar-vell) : _marcoreis@fieb.org.br_

<hr>

_For more codes visit_ [BIR - BrazilianInstituteofRobotics](https://github.com/Brazilian-Institute-of-Robotics)
_For more informations visit_ [RASC](https://www.braziliansinrobotics.com/)


## Development
**1.** Install [**ROS Noetic**](http://wiki.ros.org/noetic/Installation/Ubuntu).

**2.** Create a workspace, clone this repository and build the workspace.
```
pc remoto
$ roscore
$ export TURTLEBOT3_MODEL=burger
$ roslaunch turtlebot3_slam turtlebot3_slam.launch
$ export TURTLEBOT3_MODEL=burger
$ roslaunch turtlebot3_teleop turtlebot3_teleop_key.launch
$ rosrun map_server map_saver -f ~/map
```
```
$ export TURTLEBOT3_MODEL=burger
$ roslaunch turtlebot3_navigation turtlebot3_navigation.launch map_file:=$HOME/map.yaml
```
$ roslaunch turtlebot3_autorace_camera intrinsic_camera_calibration.launch
$ roslaunch turtlebot3_autorace_camera extrinsic_camera_calibration.launch
$ roslaunch turtlebot3_autorace_detect detect_sign.launch mission:=SELECT_MISSION
$ rqt_image_view
```
turtle
$ ssh ubuntu@10.88.119.10
$ export TURTLEBOT3_MODEL=burger
$ roslaunch turtlebot3_bringup turtlebot3_robot.launch
$ roslaunch turtlebot3_autorace_camera raspberry_pi_camera_publish.launch
```
**3.** Initialize the simulation
```
$ source /ardrone_ws/devel/setup.bash
$ roslaunch ardrone_challenge challenge.launch
```
**4.** Inicialize the node
```
$ source /ardrone_ws/devel/setup.bash
$ rosrun ardrone_challenge drone_move.py
```
**5.** If you want to compare the real position of the drone with the one it is in the node
```
$ rostopic echo /ardrone/gt_pose
```
The node positions are printed while the node is running.