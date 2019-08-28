#!/usr/bin/python3

import sys
import argparse
import json
import requests
import shutil

#TODO:
# Add doc strings
# Add function and arguments to get a list of dates
# Add output path argument
# Date string should be checked for formatting, and should not precede the oldest image or exceed today's date.

parser = argparse.ArgumentParser(description="Simple CLI app that takes a NASA API key and grabs the APOD for today, or the specified date, and downloads it to the current directory.")
parser.add_argument("--api_key", help="The api.nasa.gov API key to use. Defaults to DEMO_KEY", default='DEMO_KEY')
parser.add_argument("--date", help="The date to grab the photo from. Defaults to today.")
args = parser.parse_args()

if args.api_key:
    API_KEY = args.api_key
else:
    API_KEY = 'DEMO_KEY'

if args.date:
    date = '&date=' + args.date
else:
    date = '&date=today'

endpoint = 'https://api.nasa.gov/planetary/apod?api_key='
api_url = endpoint + API_KEY + date

def getAPOD():
    response = (requests.get(api_url))

    if response.status_code == 200:
        return response.json()['url']
    else:
        print("There was an error talking to the API.")

def downloadAPOD(url):
    response = requests.get(url, stream=True)
    filename = url.rsplit('/', 1)[-1]

    with open(filename, 'wb') as image:
        shutil.copyfileobj(response.raw, image)
    del response

APOD = getAPOD()
downloadAPOD(APOD)
