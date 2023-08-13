import pyowm 
import yaml
from utility.read_yaml import read_api_keys

def get_weather(api_key, city="Kathmandu"):
    owm = pyowm.OWM(api_key)
    mgr = owm.weather_manager()
    
    observation = mgr.weather_at_place(city)
    w = observation.weather

    temperature = w.temperature('celsius')["temp"]
    weather_description = w.detailed_status
    
    return temperature, weather_description

def get_temperature():
    api_keys = read_api_keys("config.yml")
    weather_api_key = api_keys['weather_api_key']
    temp, weather =  get_weather(weather_api_key)
    return "Temperature right now is: " + str(temp)