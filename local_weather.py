import datetime
import requests

api_key = "[Your Key]"
location = "[Your City ,Your Country]"

def get_weather(api_key, location):
    url = "https://api.openweathermap.org/data/2.5/weather"
    
    querystring = {"q":location,
                   "appid":api_key,
                   "units":"metric"}
    
    
    response = requests.request("GET", url, params=querystring)

    frame = response.json()

    
    ts = datetime.datetime.fromtimestamp(frame['dt']).strftime('%Y-%m-%dT%H:%M:%SZ')
    
    return ts,str(frame['main']['temp'])\
           ,str(frame['main']['feels_like'])\
           ,str(frame['main']['humidity'])\
           ,str(frame['main']['pressure'])\
           ,str(frame['wind']['speed'])\
           ,str(frame['wind']['deg'])\
           ,str(frame['rain']['1h'])\
           ,frame['weather'][0]['main']\
           ,frame['weather'][0]['description']\
           ,str(frame['clouds']['all'])\
           

if __name__ == "__main__":
    print(get_weather(api_key, location))


