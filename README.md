# HomeSensing
This project is a home sensing arrangement using Raspberry PI's, sensors, MQTT and MongoDB to capture data around the house and store it for future analysis.

# ToDo
1. Write the instructions.
1. Rename "pub_cpu_temp.py" to something more generic i.e. "pub_data_to_mqtt.py"

# Setup
1. Install mosquitto (MQTT broker), and mosquitto_client (MQTT client for testing).
1. Install MongoDB
1. PIP(3) Install Python modules
  1. ...

# Brief Instructions
1. pub_cpu_temp.py to run on cron job every xx minutes. (Remove lines for services not used).
2. toDb.py to run as a Daemon which shall auto start on boot. (Bash script mqttToDb.sh must be add to etc/init.d/ and run various commands - see link in thanks).

# Architecture
![Architecture](arch.jpg)

# Thanks
Some of the ideas here were taken from a blog by Lars - thanks Lars - here is the [link](https://thingsmatic.com/2016/06/18/daemonize-that-python-script/)
