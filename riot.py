class basic_info(user_name):
	api_key = 'b0afea27-1602-4ed8-aff5-24caf6bbb2d1'

	def fetch(self):
		payload = {'api_key': api_key}

		s_info = requests.get("https://na.api.pvp.net/api/lol/na/v1.4/summoner/by-name/{}".format(user_name), params=payload) #format the API request URL