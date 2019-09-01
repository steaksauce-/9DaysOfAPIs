#!/usr/bin/python

import json
import argparse
import requests
import getpass
import random

parser = argparse.ArgumentParser(description="Returns a random message from FOAAS that only requires input in the from field.")
parser.add_argument("--signed", help="Who are you?")
args = parser.parse_args()

possible_messages = ["asshole", "awesome", \
"bag", "because", "bucket", "bye", "cool", "cup", \
"diabetes", "everyone", "everything", "family", "fascinating", \
"flying", "ftfy", "fyyff", "give", "horse", "immensity", \
"jinglebells", "life", "logs", "looking", "maybe", "me", \
"mornin", "no", "pink", "programmer", "question", "ratarse", \
"retard", "ridiculous", "rtfm", "sake", "shit", "single", \
"thanks", "that", "this", "too", "tucker", "what", "zayn", "zero"]

api_endpoint = "http://foaas.com/"

headers = {'Accept': 'text/plain'}

def getMessage():
    if args.signed:
        signed = args.signed
    else:
        signed = getpass.getuser()

    message = random.choice(possible_messages)

    api_url = api_endpoint + message + "/" + signed

    response = requests.get(api_url, headers = headers)

    if response:
        print(response.text)
    else:
        print("There was an error.")

def testMessgaes():
    signed = getpass.getuser()

    for message in possible_messages:
        api_url = api_endpoint + message + "/" + signed

        print(requests.get(api_url, headers = headers).text)



getMessage()