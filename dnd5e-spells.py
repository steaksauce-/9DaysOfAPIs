#!/usr/bin/python3

import requests
import json
import argparse

parser = argparse.ArgumentParser(description="Grabs information about a given Dungeons and Dragons 5e Spell")
parser.add_argument("spell_name", help="The name of the spell to get information for.")
args = parser.parse_args()

endpoint = 'http://dnd5eapi.co/api/spells/'
spell_name = '?name=' + args.spell_name.replace(" ", "+")
url = endpoint + spell_name

def getSpellInfo():
    response = requests.get(url)

    if response:
        if (response.json()['count'] == 0):
            print("Spell not found. Check capitalization and spelling.")
        else:
            spellUrl = response.json()['results'][0]['url'] + spell_name
            response = requests.get(spellUrl)
            if response:
                response = response.json()
                spell_classes = []
                for class_entry in response['classes']:
                    spell_classes.append(class_entry['name'])

                def getSpellClasses():
                    class_list = str(', '.join(spell_classes))
                    return class_list

                the_class_list = getSpellClasses()

                print(f"Spell Name: {response['name']} \n\
Description: {response['desc'][0]}\n\
Higher Level: {response['higher_level'][0]}\n\
Range: {response['range']}\n\
Concentration: {response['concentration']}\n\
Casting Time: {response['casting_time']}\n\
Level: {response['level']}\n\
School: {response['school']['name']}\n\
Classes: {the_class_list}\n\n")

getSpellInfo()
