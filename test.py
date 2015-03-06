import json, requests

payload = {'api_key': 'e3ab974f-7a2f-417c-b31d-78c86c1dd190'}

r = requests.get("http://status.leagueoflegends.com/shards", params  = payload)

if r.status_code == 200:
	print("Success!")
else:
	print("Failure")
