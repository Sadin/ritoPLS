import json, requests

payload = {'api_key': 'e3ab974f-7a2f-417c-b31d-78c86c1dd190'}

r = requests.get("https://na.api.pvp.net/api/lol/na/v1.4/summoner/by-name/Ruinsane", params  = payload)

if r.status_code == 200:
	print("Success!")
else:
	print("Failure")
