"""
IDcreator uses NHL API to get an id number for each nhl player and store it in playerIDs.json.  Should only be used every now and then,
as most players will already be accounted for from previous scans
"""
masterPath = '/Users/harborwolff/desktop'
import requests
import json
import os

ID = 1

playerList = []
while ID < 56:
     API_URL = f"https://statsapi.web.nhl.com/api/v1/teams/{ID}/roster"
     response = requests.get(API_URL + f"/stats?stats=gameLog", params={"Content-Type": "application/json"})
     data = response.json()

     try:
          for player in data["roster"]:
                    print("\tAdded: " + player["person"]["fullName"] + " " + str(player["person"]["id"]) + " to playerIDs.json")
                    playerList.append({"name" : player["person"]["fullName"], "id" : player["person"]["id"]})

     except:
               print("didnt like ID: " + str(ID))
     ID += 1

os.remove(f"{masterPath}/project/jsons/playerIDs.json")
with open(f"{masterPath}/project/jsons/playerIDs.json", 'w') as fp:
    fp.write(json.dumps(playerList, indent=1))
    pass
