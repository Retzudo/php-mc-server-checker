#!/usr/bin/python3

import urllib.request
import json

class McServerChecker:
	def __init__(self, server, url):
		self._server = server
		self._url = url

	def getData(self):
		response = urllib.request.urlopen(self._url+self._server)
		data = response.read().decode("utf8")
		response.close()
		return data

	def getJson(self):
		return json.loads(self.getData())

	def check(self):
		data = self.getJson()
		print("Server is ", end="")
		if data['online']:
			print("\033[92monline\033[0m (", data['online_players'], "/", data['max_players'], ")", sep="")
			#data['online_players'] data['max_players']
		else:
			print("\033[91moffline\033[0m")