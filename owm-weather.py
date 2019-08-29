#!/usr/bin/python3

import argparse
import requests
import json

#TODO:
# provide actual forecast for rest of the day and tomorrow.
# return something if it is raining or snowing (could be useful to say if it is raining or snowing, send an SMS message to a loved one)
# Add flags for temp unit selction (kelvin, celcius, etc..)
# Add flags for country code

parser = argparse.ArgumentParser(description="Obtains weather forecast for a given city using a given API key from openweathermap.org")
parser.add_argument("api_key", help="Your OWM API key.")
parser.add_argument("zip_code", help="The zipcode you wish to query about.")
args = parser.parse_args()

API_KEY = args.api_key
zipcode = args.zip_code

api_endpoint = 'https://api.openweathermap.org/data/2.5/forecast?zip='
api_url = api_endpoint + zipcode + ',us&units=imperial&APPID=' + API_KEY

def getWeather():
    response = requests.get(api_url)

    if response:
        response = response.json()
        print(f"Currently in {response['city']['name']} : \n \
            Temperature: {response['list'][1]['main']['temp']} \n \
            Weather: {response['list'][2]['weather'][0]['description']}. \n\n")

getWeather()
