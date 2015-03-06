import requests, pprint, json



class summoner():

	def __init__(self, name):

		api_key = 'b0afea27-1602-4ed8-aff5-24caf6bbb2d1'
		payload = {'api_key': api_key}
		result = requests.get("https://na.api.pvp.net/api/lol/na/v1.4/summoner/by-name/{}".format(name), params=payload) #format the API request URL

		self.name = name
		self.status = result.status_code

	def basic_info(self, name):
		return 0

		