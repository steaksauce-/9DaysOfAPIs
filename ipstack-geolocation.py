#!/usr/bin/python3

import argparse
import json
import requests

parser = argparse.ArgumentParser(description="Returns the geolocation for your current IP address, or a given IP address.")
parser.add_argument("api_key", help="Your IP Stack API key.")
parser.add_argument("--ip", help="The IP address you wish to query. Defaults to your IP address.")
args = parser.parse_args()

API_KEY = "?access_key=" + args.api_key
api_endpoint = "http://api.ipstack.com/" 

def getCurrentIP():
    response = requests.get("http://api.ipstack.com/check" + API_KEY).json()['ip']
    return response

def getIPLocation():
    response = requests.get(api_url)

    if response:
        response = response.json()
        print(f"Location info for {ip}: {response['city']}, {response['region_name']}, {response['country_name']}")

if args.ip:
    ip = args.ip
else:
    ip = getCurrentIP()
    
api_url = api_endpoint + ip + API_KEY

getIPLocation()


