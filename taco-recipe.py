#!/usr/bin/python3

import json
import requests
import argparse

parser = argparse.ArgumentParser(description="Gives you a random taco recipe!")
args = parser.parse_args()

api_url = "http://taco-randomizer.herokuapp.com/random/?full-taco=true"

def getRecipe():
    response = requests.get(api_url)

    if response:
        response = response.json()

        recipe_name = response['slug'].replace("_", " ")
        recipe = response['recipe']

        print(f"{recipe_name} \n {recipe}")

getRecipe()