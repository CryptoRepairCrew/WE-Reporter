#!/usr/bin/python
import sys
import os
from bitcoinrpc.authproxy import AuthServiceProxy
import httplib, urllib
import settings

for x in range (0, 99):
    if hasattr(settings, 'COIN_' + str(x) + '_SYMBOL') and hasattr(settings, 'COIN_' + str(x) + '_NAME') and hasattr(settings, 'COIN_' + str(x) + '_TOKEN') and hasattr(settings, 'COIN_' + str(x) + '_HOST') and hasattr(settings, 'COIN_' + str(x) + '_PORT') and hasattr(settings, 'COIN_' + str(x) + '_USER') and hasattr(settings, 'COIN_' + str(x) + '_PASS'):
	SYMBOL = settings.__dict__['COIN_' + str(x) + '_SYMBOL']
	NAME = settings.__dict__['COIN_' + str(x) + '_NAME']
	TOKEN = settings.__dict__['COIN_' + str(x) + '_TOKEN']
	HOST = settings.__dict__['COIN_' + str(x) + '_HOST']
	PORT = settings.__dict__['COIN_' + str(x) + '_PORT']
	USER = settings.__dict__['COIN_' + str(x) + '_USER']
	PASS = settings.__dict__['COIN_' + str(x) + '_PASS']
	url = "http://" + USER + ":" + PASS + "@" + HOST + ":" + str(PORT)
	client = AuthServiceProxy(url)
	info = client.getinfo()
	
	paramlist = {
	'coin-name': NAME,
	'coin'	 : SYMBOL,
	'auth'	 : TOKEN,
	'diff'	 : info['difficulty'],
	'blocks' : info['blocks'],
	'version': info['version'],
	'protocol_version': info['protocolversion'],
	'wallet_version': info['walletversion']
	}
	if settings.__dict__['COIN_' + str(x) + '_BALANCE']:
	   paramlist['balance'] = info['balance']

	params = urllib.urlencode(paramlist)
	headers = {"Content-type":"application/x-www-form-urlencoded", "Accept": "text/plain"}
	conn = httplib.HTTPSConnection("walletexplorer.net")
	conn.request("POST", "/api/submit", params, headers)
	response = conn.getresponse()
	conn.close()
