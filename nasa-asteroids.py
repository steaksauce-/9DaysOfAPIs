#!/usr/bin/python3

import argparse
import requests
import json

# TODO:
# Check dates for proper format
# API appears to go back as far as 1900-01-01
# API only allows query for up to one week
# Check for existing dates (ie, no 2019-06-31)
# Add flags for additional available information

parser = argparse.ArgumentParser(description="Returns a list of Near Earth Objects on a given date range and notes if they are considered potentially hazardous.")
parser.add_argument("api_key", help="The API key to use.")
parser.add_argument("start_date", help="The start date that the asteroid will be near Earth. example: 2019-07-23")
parser.add_argument("end_date", help="The end date that the asteriod will be near Earth. example: 2019-08-03")
args = parser.parse_args()

API_KEY = args.api_key
start_date = args.start_date
end_date = args.end_date

api_url = 'https://api.nasa.gov/neo/rest/v1/feed?start_date=' + start_date + '&end_date=' + end_date + '&api_key=' + API_KEY

# print(api_url) # Debug

def getNearAsteroids():
    response = (requests.get(api_url))

    if response:
        response = response.json()
        for date in response['near_earth_objects']:
                print("Objects near earth on " + date + " :")
                for near_obj in response['near_earth_objects'][date]:
                        if(near_obj['is_potentially_hazardous_asteroid'] == True):
                                print(near_obj['name'] + " is estimated to be " + str(near_obj['estimated_diameter']['miles']['estimated_diameter_max']) + " miles in diameter and is classified as a potentially hazardous asteroid.")
                        else:
                                print(near_obj['name'] + " is estimated to be " + str(near_obj['estimated_diameter']['miles']['estimated_diameter_max']) + " miles in diameter.")

                print("\n\n\n")

    else:
        print("There was an error talking to the API.")

getNearAsteroids()

