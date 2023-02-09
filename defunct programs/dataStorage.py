"""
The functions that create requested data entries and also access them
"""
#TODO figure out a way to overwrite files whenever a more modern call is made
import os
from os import path
from re import L
from bs4 import BeautifulSoup
import requests

"""
Creates a new file within the storage system that contains stats for a given player in a given year.
Returns False if the requested player's file already exists, thereby skipping the operation
File format player: G A P S
Goalie: GA, SV, SV%

@param year: the year player (e.g. 19-20)
@param surname: e.g. kaprizov
@param name: e.g. kirill
"""
def createHockey(year, surname, name):
    path = f'/Users/harborwolff/desktop/dataS/hockey/{year}'
    fileName = surname + name
    longPath = path + fileName

    if os.path.exists(longPath):
        return False

    surLet = surname[0]
    pageStr = surname[0:5] + name[0:2]
    yearStr = '20'+ year[3:5]
    index = 1

    url = f'https://www.hockey-reference.com/players/{surLet}/{pageStr}0{str(index)}/gamelog/{yearStr}'
    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'html.parser')
    print(soup.prettify)

    urlName = name[0].upper() + name[1:] + " " + surname[0].upper() + surname[1:] 

    #check to make sure it's the actual player
    while len(soup.find_all('span', text = urlName)) == 0:
        index += 1
        url = f'https://www.hockey-reference.com/players/{surLet}/{pageStr}0{str(index)}/gamelog/{yearStr}'
        page = requests.get(url)
        soup = BeautifulSoup(page.text, 'html.parser')
    
    table = soup.find("table").find("tbody").find_all("tr")

    #check for goalie
    with open(os.path.join(path, fileName), 'w') as fp:
        for data in table:
            gamedata = []
            for detail in data.find_all("td"):
                bit = str(detail.string)
                gamedata.append(bit)
            if len(gamedata) > 0:
                if len(soup.find_all("th", text = 'Goalie Stats')) == 0:
                    fp.write(str(gamedata[7]) + " ") #G
                    fp.write(str(gamedata[8]) + " ") #A
                    fp.write(str(gamedata[9]) + " ") #S
                    fp.write(str(gamedata[19])+ " \n") #P
                else:
                    fp.write(str(gamedata[8]) + " ") #GA
                    fp.write(str(gamedata[9]) + " ") #SA
                    fp.write(str(gamedata[10]) + " \n") #SV




"""
Creates a stat page for a pitcher based on a year, only creates a total statline rather than a game-by-game analysis
"""            
def createBaseballPitcher(year, surname, name):
    path = f'/Users/harborwolff/desktop/dataS/baseball/{year}'
    fileName = surname + name
    longPath = path + fileName

    if os.path.exists(longPath):
        return False

    surLet = surname[0]
    pageStr = surname[0:5] + name[0:2]
    yearStr = '20'+ year[3:5]
    index = 1

    url = f'https://www.baseball-reference.com/players/{surLet}/{pageStr}0{str(index)}.shtml'
    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'html.parser')

    urlName = name[0].upper() + name[1:] + " " + surname[0].upper() + surname[1:] 

    #check to make sure it's the actual player
    while len(soup.find_all('span', text = urlName)) == 0:
        index += 1
        url = f'https://www.baseball-reference.com/players/{surLet}/{pageStr}0{str(index)}.shtml'
        page = requests.get(url)
        soup = BeautifulSoup(page.text, 'html.parser')
        
    table = soup.find("table").find("tbody").find("tr", id=f'pitching_standard.20{year}')

    #pull important stats
    with open(os.path.join(path, fileName), 'w') as fp:
        gamedata = []
        for detail in table.find_all("td"):
            bit = str(detail.string)
            gamedata.append(bit)
        if len(gamedata) > 0:                   
            fp.write(str(gamedata[6]) + " ") #ERA
            fp.write(str(gamedata[7]) + " ") #GP
            fp.write(str(gamedata[13]) + " ") #IP
            fp.write(str(gamedata[26]) + " ")  #FIP
            fp.write(str(gamedata[27]) + " ") #WHIP
            fp.write(str(gamedata[28]) + " ") #H9
            fp.write(str(gamedata[32]) + " \n") #SO9


"""
Accesses the player's file stats
PRECONDITION: file is assumed to already exist TODO make sure higher level function checks for this
TODO make sure higher function differentiates between players and goalies

@return a list of gamelists of the players stats x
"""
def accessHockey(year, surname, name):
    path = f'/Users/harborwolff/desktop/dataS/hockey/{year}/{surname}{name}'

    topArray = [] 
    with open(path, "r") as file:
        
        while True:
            line = file.readline()
            gameStats = line.split(" ")
            topArray.append(gameStats)

            pass
            if not line:
                break
        for gameday in topArray:
            del gameday[-1]
    return topArray


"""
Accesses the player's file stats
PRECONDITION: file is assumed to already exist TODO make sure higher level function checks for this
TODO make sure higher function differentiates between players and goalies

@return a list of the players stats
"""
def accessBaseball(year, surname, name):
    path = f'/Users/harborwolff/desktop/dataS/baseball/{year}/{surname}{name}'

    topArray = [] 
    with open(path, "r") as file:
        
        while True:
            line = file.readline()
            gameStats = line.split(" ")
            topArray.append(gameStats)

            pass
            if not line:
                break
        for gameday in topArray:
            del gameday[-1]
    return topArray

"""
Creates a stat page for a hockey team given a year
"""
def createHTeam(year, nameStr):
    path = f'/Users/harborwolff/desktop/dataS/hockey/{str(int(year)-1)}-{year}'
    fileName = nameStr
    url = f"https://www.hockey-reference.com/teams/{nameStr}/20{year}_gamelog.html"

    page = requests.get(url)

    soup = BeautifulSoup(page.text, 'html.parser')

    table = soup.find("table").find_all("tr")

    #date, /@/, opp, gf, ga, w/l
    gamelog = []

    for data in table:
        gamedata = []
        for detail in data.find_all("td")[3:9]:
            bit = str(detail.string)
            if bit != 'None':
                gamedata.append(bit)
        gamelog.append(gamedata)
    
    with open(os.path.join(path, fileName), 'w') as file:
        for i in range(0, len(gamelog) -1):
            if len(gamelog[i]) == 0:
                pass
            else:
                file.write(gamelog[i][0] + " ")
                file.write(gamelog[i][1] + " ")
                file.write(gamelog[i][-1] + " \n")

"""
Access the data in a hockey team's file

@return a list of the team's stats from that year
"""
def accessHTeam(year, nameStr):
    path = f'/Users/harborwolff/desktop/dataS/hockey/{str(int(year)-1)}-{year}/{nameStr}'

    topArray = [] 
    with open(path, "r") as file:
        
        while True:
            line = file.readline()
            gameStats = line.split(" ")
            topArray.append(gameStats)

            pass
            if not line:
                break
        for gameday in topArray:
            del gameday[-1]
    return topArray
    
