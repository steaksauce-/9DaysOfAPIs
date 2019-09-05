#!/usr/bin/python3

import requests
import json
import argparse
from twilio.rest import Client

parser = argparse.ArgumentParser(description="Grabs information about a given Dungeons and Dragons 5e Spell and texts it to a given number.")
parser.add_argument("spell_name", help="The name of the spell to get information for.")
parser.add_argument("api_key", help="The Twilio API key.")
parser.add_argument("auth_token", help="The Twilio acccount Auth Token.")
parser.add_argument("sender", help="The Twilio phone number to send the SMS message from.")
parser.add_argument("recipient", help="The phone number to send the spell information from.")
args = parser.parse_args()

def getSpellInfo():
    dnd_endpoint = 'http://dnd5eapi.co/api/spells/'
    spell_name = '?name=' + args.spell_name.replace(" ", "+")
    dnd_url = dnd_endpoint + spell_name
    response = requests.get(dnd_url)

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

                return str(f"Spell Name: {response['name']} Description: {response['desc'][0]} Higher Level: {response['higher_level'][0]} Range: {response['range']} Concentration: {response['concentration']} Casting Time: {response['casting_time']} Level: {response['level']} School: {response['school']['name']} Classes: {the_class_list}")

def sendSMS(body, recipient, sender, api_key, auth):
    client = Client(api_key, auth)

    message = client.messages.create(from_ = sender, body = body, to = recipient)
    print(message.sid)

print(getSpellInfo()) # Debug

sendSMS(getSpellInfo(), args.recipient, args.sender, args.api_key, args.auth_token)
