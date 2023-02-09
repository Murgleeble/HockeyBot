import requests
import json
import os

ID = 1

playerList = []
while ID < 55:
     API_URL = f"https://statsapi.web.nhl.com/api/v1/teams/{ID}/roster"
     response = requests.get(API_URL + f"/stats?stats=gameLog", params={"Content-Type": "application/json"})
     data = response.json()

     try:
          for player in data["roster"]:
                    #print("\t" + player["person"]["fullName"] + " " + str(player["person"]["id"]))
                    playerList.append({"name" : player["person"]["fullName"], "id" : player["person"]["id"]})

     except:
               print("didnt like ID: " + str(ID))
     ID += 1

os.remove("/Users/harborwolff/desktop/project/playerIDs.json")
with open("/Users/harborwolff/desktop/project/playerIDs.json", 'w') as fp:
    fp.write(json.dumps(playerList, indent=1))
    pass
