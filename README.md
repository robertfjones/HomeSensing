# HomeSensing
This project is a home sensing arrangement using Raspberry PI's, sensors, MQTT and MongoDB to capture data around the house and store it for future analysis.

# ToDo
1. Write the instructions.
1. Rename "pub_cpu_temp.py" to something more generic i.e. "pub_data_to_mqtt.py"
1. Add and commit daemon bash script.

# Setup
1. Install mosquitto (MQTT broker), and mosquitto_client (MQTT client for testing).
1. Install MongoDB
1. PIP(3) Install Python modules
  1. ...

# Brief Instructions
1. pub_cpu_temp.py to run on cron job every xx minutes. (Remove lines for services not used).
2. toDb.py to run as a Daemon which shall auto start on boot. (Bash script mqtt.sh to be committed soon then user must add to etc/init.d/ and run various commands).

# Architecture
![Architecture](arch.jpg)
