"""
nhlAPI uses Webdriver to get the daily lines, then create a .csv file for each player's seasonal performance that is
used to calculate inferential and simple statistics
"""
masterPath = '/Users/harborwolff/desktop'
import requests
import json
import os
from webdriver import getLines

def lines():
     #read in IDs file
     filePath = f"{masterPath}/project/jsons/playerIDs.json"
     with open(filePath, 'r') as j:
          contents = json.loads(j.read())
     ID = 0

     #remove once lines are independently gathered
     getLines()

     jsonPath = f'{masterPath}/project/jsons/dailyLines.json'
     with open(jsonPath, 'r') as jp:
          dailyLines = json.loads(jp.read())

     for item in dailyLines:
          try:
               name = item['name'].split(' ')

               #get the player id
               for key in contents:
                    if key["name"].lower() == (name[0] + ' ' + name[1]).lower():
                         ID = key["id"]

               API_URL = f"https://statsapi.web.nhl.com/api/v1/people/{ID}"
               response = requests.get(API_URL + f"/stats?stats=gameLog", params={"Content-Type": "application/json"})
               data = response.json()

               path = f'{masterPath}/dataS/hockey/22-23'
               fileName = name[1].lower() + name[0].lower() + ".csv"
               longPath = path + fileName

               with open(os.path.join(path, fileName), 'w') as fp:
                    for item in data['stats'][0]['splits']:
                              fp.write(item['date'] + ',' + str(item['stat']['goals']) + ',' + str(item['stat']['assists']) + ',' + str(item['stat']['shots']) + ',' + str(item['stat']['hits']) + ',' + str(item['stat']['blocked']))
                              fp.write('\n')
          except(KeyError):
               print("Couldn't parse player: " + name[0] + " " + name[1] + ". \nConsider re-running idCreator to update the list")
