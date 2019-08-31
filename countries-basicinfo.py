#!/usr/bin/python3

import argparse
import json
import requests

parser = argparse.ArgumentParser(description="Gives the capital and language(s) of a given country.")
parser.add_argument("country", help="The full name of the country.")
args = parser.parse_args()

api_endpoint = "https://restcountries.eu/rest/v2/name/"

def getCountryInfo():
    country = args.country

    api_url = api_endpoint + country + "?fullText=true"

    response = requests.get(api_url).json()
    response = response[0]
    
    if response:
        languages = []
        i = 0
        while i < len(response['languages']):
            languages.append(response['languages'][i]['name'])
            i += 1
        languages = ", ".join(languages)

        print(f"The capital of {country} is {response['capital']}. In {country}, they speak {languages}")

getCountryInfo()


