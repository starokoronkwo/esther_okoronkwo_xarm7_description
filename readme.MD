# Ufactory Xarm7 - Task 4

## Project Overview 
This task focuses on the developmenr of a complete URDF model for the xArm7 robotic manipulator.

## Tools Used
- ROS 2 Humble
- Rviz2
- MeshLab
- VS Code
- Git and Github
- colcon build

## Installation
### 1. Install ROS2 Humble
You can follow [this guide](https://docs.ros.org/en/humble/Installation.html) to do that.
### 2. Install Required ROS Packages
```
sudo apt install ros-humble-xacro \
ros-humble-joint-state-publisher \
ros-humble-joint-state-publisher-gui \
ros-humble-robot-state-publisher \
ros-humble-rviz2 -y
```
### 3. Create and Build the Workspace
```
# Create workspace
mkdir -p ~/task4_ws/src
cd ~/task4_ws/src

# Clone your URDF package
git clone <your_repo_link_here>

# Go back to workspace root and build
cd ~/task4_ws
colcon build

# Source the workspace
source install/setup.bash
```
### 4. Launch Rviz with the Xarm7 URDF
```
ros2 launch urdf_tutorial display.launch.py model:=$PWD/src/ufractor_xarm7/urdf/ufactory_xarm7.urdf
```

## Challenges and What I Learned
### 1. Path Issues
The workspace folder contained spaces which causes launch argument parsing errors.
### 2. "No transform" errors - Rviz couldn't TF frames
robot_state_publisher wasn't running or wasn't receiving robot_description; Fixed Frame set to base_link but frame didn't exist in TF tree.
What I learnt: I learnt the role of robot_state_publisher, it publisfes TF transforms between links based on the robot's URDF. Without it, RViz can't display the robot model or compute transformations.
### 3. Joint sliders not appearing in joint_state_publisher_gui
Invalid axis definitions like ``` axis xyz = "0 0 0" ```; Wrong joint types or missing limit tags
What I learnt: I learnt how joint_state_publisher_gui works- it only creates sliders for revolute or prismatic joints that have valid, non-zero axes and proper limit ranges.
### 4. Disconnected motion - moving one joint didn't carry child links
Incorrect joint origins and orientations; Misaligned parent-child relationships.
What I learnt: I learnt the importance of correct joint origins and orientations. They define how links are physically connected and how motion is transferred in the TF tree. Proper alignment ensures realistic kinematic behaviour.

## Final Results
[![Screenshot-from-2025-11-01-03-19-21.png](https://i.postimg.cc/L53Wj0TR/Screenshot-from-2025-11-01-03-19-21.png)](https://postimg.cc/LghvpDw0)
[![Screenshot-from-2025-11-01-03-19-58.png](https://i.postimg.cc/W368yqJ5/Screenshot-from-2025-11-01-03-19-58.png)](https://postimg.cc/phrKhTCj)

## Side Quest(s) (kinda)
Got carried away trying to understand some things, I just ended up more confused.
### DH Parameters
DH(Denavit-Hartenberg) parameters are uded to calculate kinematics of UR robots. It describes the geometry of robot links and joints using four values - theta, d, a and alpha. Each set of parameters defines how one joint's coordinate frame is positioned and oriented relative to the previous one.
The Modified DH convention (used for xArm7) slightly differs from the standard one in how transformations are ordered, which affects how the URDF's origins and rotations are computed.

![Modified DH Parameters Matrix](https://wikimedia.org/api/rest_v1/media/math/render/svg/c871f4e80e3c6be1cebb018cfb71de2f12e9e340)

### DH Table:
1. The DH table is usually given in millimeters, but URDF requires meters.
2. alpha defines rotation about the X-axis(corresponds to the roll in rpy).
3. d is the offset along the Z-axis of the parent frame.
4. a is the offset along the X-axis of the parent frame.
5. theta correspinds to the joint's rotational variable for revolute joints

![UFACTORY xArm7 Modified D-H Parameters](https://downloads.intercomcdn.com/i/o/236300733/645151bc930f525ad4688f4e/01.jpg?expires=1762195500&signature=6fe47559feb7ef708bf9d9441cc674ea60274f8786753a031255745fd70e243c&req=diMhFcl%2BmoJcFb4f3HP0gIMOkeftIM%2F4EDc18m9vIcmIGSfOl9c0PkNwo6um%0Af%2Bizx%2BnX1%2B7ZathYUw%3D%3D%0A)

## Resources and References:
1. [Denavit–Hartenberg parameters](https://en.wikipedia.org/wiki/Denavit%E2%80%93Hartenberg_parameters)
2. [Kinematic and Dynamic Parameters of UFACTORY xArm Series](https://help.ufactory.cc/en/articles/4330809-kinematic-and-dynamic-parameters-of-ufactory-xarm-series)
3. [Specification for xArm](http://download.ufactory.cc/xarm/en/Specification%20for%20xArm_20191021.pdf)
4. [ROS2 URDF Tutorials](https://docs.ros.org/en/humble/Tutorials/Intermediate/URDF/URDF-Main.html)
