"""
inferential does all of the z-score calculations on player statistics, and is the core of the math for the program
"""
masterPath = '/Users/harborwolff/desktop'
import os
import math as m
from scipy.stats import norm


"""
Returns a list of lists containing stats per gameday
"""
def accessData(firstname, lastname):
    path = f"{masterPath}/dataS/hockey/22-23/{lastname.lower()}{firstname.lower()}.csv"

    try:
        topArray = [] 
        with open(path, "r") as file:
            while True:
                line = file.readline()
                gameStats = line.split(",")
                topArray.append(gameStats)

                pass
                if not line:
                    break
    except:
        print("path does not exist")
        return False
    return topArray

def getStatsHelper(firstname, lastname):
    path = f'/Users/harborwolff/desktop/dataS/hockey/22-23/{lastname.lower()}{firstname.lower()}.csv'
    finalList = []

    if not os.path.exists(path):
        print("file not found")
        return False
    data = accessData(firstname, lastname)
    if data == False:
        return False

    sumG = 0
    sumA = 0
    sumS = 0
    sumH = 0
    sumB = 0
    counter = 0
    for i in range(0, len(data)-1):
        sumG += int(data[i][1])
        sumA += int(data[i][2])
        sumS += int(data[i][3])
        sumH += int(data[i][4])
        sumB += int(data[i][5])
        counter += 1
    meanG = sumG/counter
    meanA = sumA/counter
    meanS = sumS/counter
    meanH = sumH/counter
    meanB = sumB/counter

    finalList.append(meanG)
    finalList.append(meanA)
    finalList.append(meanS)
    finalList.append(meanH)
    finalList.append(meanB)

    return finalList

def getStats(firstname, lastname):
    path = f'/Users/harborwolff/desktop/dataS/hockey/22-23/{lastname.lower()}{firstname.lower()}.csv'
    finalList = []
    if not os.path.exists(path):
        print("file not found")
        return False

    playerMeans = getStatsHelper(firstname, lastname)
    if playerMeans == False:
        return False
    data = accessData(firstname, lastname)
    if accessData == False:
        return False

    cSumG = 0
    cSumA = 0
    cSumS = 0
    cSumH = 0
    cSumB = 0

    for i in range(0, len(data) - 1):
        cSumG += (int(data[i][1])-playerMeans[0])**2
        cSumA += (int(data[i][2])-playerMeans[1])**2
        cSumS += (int(data[i][3])-playerMeans[2])**2
        cSumH += (int(data[i][4])-playerMeans[3])**2
        cSumB += (int(data[i][5])-playerMeans[4])**2

    finalG = m.sqrt(cSumG/(len(data)-1))
    finalA = m.sqrt(cSumA/(len(data)-1))
    finalS = m.sqrt(cSumS/(len(data)-1))
    finalH = m.sqrt(cSumH/(len(data)-1))
    finalB = m.sqrt(cSumB/(len(data)-1))

    finalList.append([playerMeans[0], finalG])
    finalList.append([playerMeans[1], finalA])
    finalList.append([playerMeans[2], finalS])
    finalList.append([playerMeans[3], finalH])
    finalList.append([playerMeans[3], finalB])

    return finalList

def inferHockeyG(firstname, lastname, line, over):
    list = getStats(firstname, lastname)
    if list == False:
        return False
    mean = list[0][0]
    sd = list[0][1]


    zscore = (line - mean)/sd
    if over == True:
        return 1 - norm.cdf(zscore)
    else:
        return norm.cdf(zscore)

def inferHockeyA(firstname, lastname, line, over):
    list = getStats(firstname, lastname)
    if list == False:
        return False
    mean = list[1][0]
    sd = list[1][1]


    zscore = (line - mean)/sd
    if over == True:
        return 1 - norm.cdf(zscore)
    else:
        return norm.cdf(zscore)

def inferHockeyS(firstname, lastname, line, over):
    list = getStats(firstname, lastname)
    if list == False:
        return False
    mean = list[2][0]
    sd = list[2][1]


    zscore = (line - mean)/sd
    if over == True:
        return 1 - norm.cdf(zscore)
    else:
        return norm.cdf(zscore)

def inferHockeyH(firstname, lastname, line, over):
    list = getStats(firstname, lastname)
    if list == False:
        return False
    mean = list[3][0]
    sd = list[3][1]


    zscore = (line - mean)/sd
    if over == True:
        return 1 - norm.cdf(zscore)
    else:
        return norm.cdf(zscore)

def inferHockeyB(firstname, lastname, line, over):
    list = getStats(firstname, lastname)
    if list == False:
        return False
    mean = list[4][0]
    sd = list[4][1]


    zscore = (line - mean)/sd
    if over == True:
        return 1 - norm.cdf(zscore)
    else:
        return norm.cdf(zscore)