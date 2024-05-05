
# Downloading ROS Noetic

**1. **Setup your computer to accept software from packages.ros.org****

 ```
 sudo sh -c 'echo "deb http://packages.ros.org/ros/ubuntu $(lsb_release -sc) main" > /etc/apt/sources.list.d/ros-latest.list'
 ```

**2. **Install cURL****

```
sudo apt install curl # if you haven't already installed curl 
curl -s https://raw.githubusercontent.com/ros/rosdistro/master/ros.asc | sudo apt-key add -
```

**3. Make sure your package is up-to date:**

```
sudo apt update
```

**4. Install ROS**

```
sudo apt install ros-noetic-desktop-full
```

**5. Source ROS Noetic**

```
echo "source /opt/ros/noetic/setup.bash" >> ~/.bashrc
source ~/.bashrc
```

**6. Install the dependencies**

```
sudo apt install python3-rosdep python3-rosinstall python3-rosinstall-generator python3-wstool build-essential
```

**7. Initialize Rosdep**

```
sudo rosdep init
rosdep update
```

**8. Check if ros is installed correctly**

```
rosversion -d
```


