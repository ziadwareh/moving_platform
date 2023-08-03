# moving_platform
This ROS package enables you to spawn two types of platforms in Gazebo. The models are:
* Landing_base
* Landing_station
  
The landing_base consists of a block in Gazebo that serves as a landing base for a UAV. On the other hand, the Landing_station consists of both the base and a block it is attached to. This is just a variety of structures that can be utilized by the user. There are two modes for each platform:
* moving
* fixed
## Installing Package
1. If you do not have a catkin_ws setup then:
```
$ mkdir -p ~/catkin_ws/src
$ cd ~/catkin_ws/
$ catkin_make #initialize your catkin_ws
```
2. Clone the git repository
```
$ cd ~/catkin_ws/src
$ git clone https://github.com/ziadwareh/moving_platform.git
$ cd ..
$ catkin_make
```
3. Source the setup.bash file.
```
$ source ~/catkin_ws/devel/setup.bash
```
## Launching model
There are two launch options, one that will launch Gazebo with it, and another that will not. Both files take 6 parameters:
* model_name: Landing_base or Landing_station. Default is landing_base.
* motion_type: moving or fixed. Default is fixed.
* x: x offset between urdf model origin and Gazebo origin. Default 0.
* y: y offset between urdf model origin and Gazebo origin. Default 0.
* z: z offset between urdf model origin and Gazebo origin. Default 0.
* enable_rviz: true or false. This is to display urdf on rviz. default is false

To launch the file with Gazebo:
```
$ roslaunch moving_platform launch_platform_model_in_gazebo.launch model_name:=landing_station enable_rviz:=true motion_type:=moving x:=1 y:=1 z:=0
```
> **Note** For the launch file without Gazebo replace `launch_platform_model_in_gazebo.launch` with `launch_platform_alone.launch`.
