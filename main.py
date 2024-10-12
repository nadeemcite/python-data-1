import requests

r = requests.get("http://ip-api.com/json")

print(r.json())