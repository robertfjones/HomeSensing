#!/usr/bin/env python3
import paho.mqtt.publish as publish
from subprocess import check_output
from re import findall
import read_room_temp as r
import local_weather

t, h = r.read_sensor()

api_key = "7928e8a0365293816970a373044ee894"
location = "Bearsden,UK"

def get_temp():
    temp = check_output(["vcgencmd","measure_temp"]).decode("UTF-8")
    return(findall("\d+\.\d+",temp)[0])

def publish_message(topic, message):
    print("Publishing to MQTT topic: " + topic)
    print("Message: " + message)

    publish.single(topic, message, hostname="192.168.1.39")

temp = get_temp()
weather_ts, weather_temp, weather_feelslike, weather_humidity\
            , weather_pressure, wind_speed, wind_dir\
            , rain, weather_main, weather_desc\
            , clouds = local_weather.get_weather(api_key, location)
publish_message("Home/MasterNode/CPUTemp", temp)
publish_message("Home/MasterNode/ExtTemp", weather_temp)
publish_message("Home/MasterNode/ExtHum", weather_humidity)
publish_message("Home/MasterNode/ExtPres", weather_pressure)
publish_message("Home/MasterNode/ExtFeelsTemp", weather_feelslike)
publish_message("Home/MasterNode/ExtWindSpeed", wind_speed)
publish_message("Home/MasterNode/ExtWindDir", wind_dir)
publish_message("Home/MasterNode/ExtCloudCover", clouds)
publish_message("Home/MasterNode/ExtRain", rain)
publish_message("Home/MasterNode/ExtWeatherMain", weather_main)
publish_message("Home/MasterNode/ExtWeatherDesc", weather_desc)
publish_message("Home/MasterNode/RoomTemp", str(t))
publish_message("Home/MasterNode/RoomHum", str(h))



