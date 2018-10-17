#!/usr/bin/env python3
import sys
import requests
import json

# Script to get access token from Telsa.  It requires the username (email address)
# and password that is normally used to log into your account on the Tesla website.

arguments = len(sys.argv) - 1
if arguments < 2:
	print ("usage: ", sys.argv[0]," email password")
	sys.exit()

r = requests.post('https://owner-api.teslamotors.com/oauth/token',
	data = {'grant_type':'password',
	'client_id':'e4a9949fcfa04068f59abb5a658f2bac0a3428e4652315490b659d5ab3f35a9e',
	'client_secret':'c75f14bbadc8bee3a7594412c31416f8300256d7668ea7e6e7f06727bfb9d220',
	'email':sys.argv[1],
	'password':sys.argv[2]})

results = json.loads(r.text)

print (results['access_token'])
