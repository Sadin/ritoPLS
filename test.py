import json, requests

region = raw_input('Which server would you like to know the status of? (ex. na, euw, oce, ect.): ')

payload = {'api_key': 'e3ab974f-7a2f-417c-b31d-78c86c1dd190'}

r = requests.get("http://status.leagueoflegends.com/shards/{}".format(region), params  = payload)

if r.status_code == 200:
	print("Congratulations! The {} server is running!".format(region))
else:
	print("I'm sorry, the {} server is currently down.".format(region))
