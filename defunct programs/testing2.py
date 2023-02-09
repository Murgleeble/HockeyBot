import requests


API_URL = f"https://statsapi.web.nhl.com/api/v1/people/8478507"
response = requests.get(API_URL + f"/stats?stats=gameLog", params={"Content-Type": "application/json"})
data = response.json()

print(data)