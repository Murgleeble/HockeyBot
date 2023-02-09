"""
The functions that will take pre-existing data files and perform a statistical analysis

TODO all baseball inferences
"""
from zlib import Z_NO_COMPRESSION
import dataStorage as ds
import os
import math as m
from scipy.stats import norm

"""
Gets the mean of a dataset, used only for hockey ATM

@param name is 0 if searching for a team
@param surname is the team's string if searching for a team
@return a list of each respective mean
"""
def getMean(year, surname, name):
    if name == 0:
        #Team stats
        path = f'/Users/harborwolff/desktop/dataS/hockey/{str(int(year)-1)}-{year}/{surname}'
        finalList = []

        #make sure the path exists before accessing
        if not os.path.exists(path):
            ds.createHTeam(year, surname)
            data = ds.accessHTeam(year, surname)
        else:
            data = ds.accessHTeam(year, surname)

        sumGF = 0
        sumGA = 0
        sumS = 0
        counter = 0
        for i in range(0, len(data)-1):
            sumGF += int(data[i][0])
            sumGA += int(data[i][1])
            sumS += int(data[i][2])
            counter += 1
        meanGF = sumGF/counter
        meanGA = sumGA/counter
        meanS = sumS/counter

        finalList.append(meanGF)
        finalList.append(meanGA)
        finalList.append(meanS)

        return finalList

    else:
        #player stats
        path = f'/Users/harborwolff/desktop/dataS/hockey/{year}/{surname}{name}'
        finalList = []

        #create 2d array with the stats, regardless of sport
        if not os.path.exists(path):
            ds.createHockey(year, surname, name)
            data = ds.accessHockey(year, surname, name)
        else:
            data = ds.accessHockey(year, surname, name)

        #separate by goalie and player
        if len(data[0]) == 3:
            #this is a goalie
            sumGA = 0
            sumSA = 0
            sumSV = 0
            counter = 0
            for i in range(0, len(data)-1):
                sumGA += int(data[i][0])
                sumSA += int(data[i][1])
                sumSV += int(data[i][2])
                counter += 1
            meanGA = sumGA/counter
            meanSA = sumSA/counter
            meanSV = sumSV/counter

            finalList.append(meanGA)
            finalList.append(meanSA)
            finalList.append(meanSV)

        else:
            #this is a player
            sumG = 0
            sumA = 0
            sumP = 0
            sumS = 0
            counter = 0
            for i in range(0, len(data)-1):
                sumG += int(data[i][0])
                sumA += int(data[i][1])
                sumP += int(data[i][2])
                sumS += int(data[i][3])
                counter += 1
            meanG = sumG/counter
            meanA = sumA/counter
            meanS = sumS/counter
            meanP = sumP/counter

            finalList.append(meanG)
            finalList.append(meanA)
            finalList.append(meanS)
            finalList.append(meanP)
        return finalList

"""
Gets the standard deviation for each individual stat on a player, used only for Hockey ATM

same specific parameters for the getMean
@return a list of tuples containing each mean and sd
"""
def getStandardDeviation(year, surname, name):
    if name == 0:
        #this is a team
        path = f'/Users/harborwolff/desktop/dataS/hockey/{str(int(year)-1)}-{year}/{surname}'
        finalList = []

        teamMeans = getMean(year, surname, 0)
        data = ds.accessHTeam(year, surname)

        cSumGF = 0
        cSumGA = 0
        cSumS = 0
        for i in range(0, len(data) - 1):
            cSumGF += (int(data[i][0])-teamMeans[0])**2
            cSumGA += (int(data[i][1])-teamMeans[1])**2
            cSumS += (int(data[i][2])-teamMeans[2])**2

        finalGF = m.sqrt(cSumGF/len(data)-1)
        finalGA = m.sqrt(cSumGA/len(data)-1)
        finalS = m.sqrt(cSumS/len(data)-1)

        finalList.append([teamMeans[0], finalGF])
        finalList.append([teamMeans[1], finalGA])
        finalList.append([teamMeans[2], finalS])

        return finalList
        
    else:
        path = f'/Users/harborwolff/desktop/dataS/hockey/{year}/{surname}{name}'
        finalList = []

        playerMeans = getMean(year, surname, name)
        data = ds.accessHockey(year, surname, name)

        if len(playerMeans) == 3:
            #this is a goalie
            cSumGA = 0
            cSumSA = 0
            cSumSV = 0
            for i in range(0, len(data) - 1):
                cSumGA += (int(data[i][0])-playerMeans[0])**2
                cSumSA += (int(data[i][1])-playerMeans[1])**2
                cSumSV += (int(data[i][2])-playerMeans[2])**2

            finalGA = m.sqrt(cSumGA/len(data)-1)
            finalSA = m.sqrt(cSumSA/len(data)-1)
            finalSV = m.sqrt(cSumSV/len(data)-1)

            finalList.append([playerMeans[0], finalGA])
            finalList.append([playerMeans[1], finalSA])
            finalList.append([playerMeans[2], finalSV])
        else:
            #this is a player
            cSumG = 0
            cSumA = 0
            cSumP = 0
            cSumS = 0
            for i in range(0, len(data) - 1):
                cSumG += (int(data[i][0])-playerMeans[0])**2
                cSumA += (int(data[i][1])-playerMeans[1])**2
                cSumP += (int(data[i][2])-playerMeans[2])**2
                cSumS += (int(data[i][3])-playerMeans[3])**2

            finalG = m.sqrt(cSumG/(len(data)-1))
            finalA = m.sqrt(cSumA/(len(data)-1))
            finalP = m.sqrt(cSumP/(len(data)-1))
            finalS = m.sqrt(cSumS/(len(data)-1))

            finalList.append([playerMeans[0], finalG])
            finalList.append([playerMeans[1], finalA])
            finalList.append([playerMeans[2], finalS])
            finalList.append([playerMeans[3], finalP])
        return finalList

"""
Run an inferential test on a goalie's GA

@param over is BOOLEAN ONLY
@return the probability that the goalie lets in more than the line of goals
"""
def inferHockeyGA(year, surname, name, line, over):
    list = getStandardDeviation(year, surname, name)
    mean = list[0][0]
    sd = list[0][1]


    zscore = (line - mean)/sd
    if over == True:
        return 1 - norm.cdf(zscore)
    else:
        return norm.cdf(zscore)

"""
Run an inferential test on a goalie's SV

@return the probability that the goalie makes more than the line amount of saves
"""
def inferHockeySV(year, surname, name, line, over):
    list = getStandardDeviation(year, surname, name)
    mean = list[2][0]
    sd = list[2][1]

    zscore = (line - mean)/sd
    if over == True:
        return 1 - norm.cdf(zscore)
    else:
        return norm.cdf(zscore)

"""
Run an inferential test on a player's G

@return the probability that the player gets more than the line of goals
"""
def inferHockeyG(year, surname, name, line, over):
    list = getStandardDeviation(year, surname, name)
    mean = list[0][0]
    sd = list[0][1]

    zscore = (line - mean)/sd
    if over == True:
        return 1 - norm.cdf(zscore)
    else:
        return norm.cdf(zscore)

"""
Run an inferential test on a player's A

@return the probability that the player gets more than the line of assists
"""
def inferHockeyA(year, surname, name, line, over):
    list = getStandardDeviation(year, surname, name)
    mean = list[1][0]
    sd = list[1][0]

    zscore = (line - mean)/sd
    if over == True:
        return 1 - norm.cdf(zscore)
    else:
        return norm.cdf(zscore)

"""
Run an inferential test on a player's S

@return the probability that the player gets more than the line of shots
"""
def inferHockeyS(year, surname, name, line, over):
    list = getStandardDeviation(year, surname, name)
    mean = list[2][0]
    sd = list[2][1]
    print("mean: " + str(mean) + " sd: " + str(sd))

    zscore = (line - mean)/sd
    if over == True:
        return 1 - norm.cdf(zscore)
    else:
        return norm.cdf(zscore)

"""
Run an inferential test on a player's P

@return the probability that the player gets more than the line of points
"""
def inferHockeyP(year, surname, name, line, over):
    list = getStandardDeviation(year, surname, name)
    mean = list[3][0]
    sd = list[3][1]

    zscore = (line - mean)/sd
    if over == True:
        return 1 - norm.cdf(zscore)
    else:
        return norm.cdf(zscore)
"""
Run an inferential test on a team's SOG

@return probability
"""
def inferHockeySOG(year, team, line, over):
    list = getStandardDeviation(year, team, 0)
    mean = list[2][0]
    sd = list[2][1]

    zscore = (line - mean)/sd
    #print("mean: " + str(mean) + " sd: " + str(sd))
    if over == True:
        return 1 - norm.cdf(zscore)
    else:
        return norm.cdf(zscore)

"""
Run an inferential test on a team's GF

@return probability
"""
def inferHockeyGF(year, team, line, over):
    list = getStandardDeviation(year, team, 0)
    mean = list[0][0]
    sd = list[0][1]

    zscore = (line - mean)/sd
    if over == True:
        return 1 - norm.cdf(zscore)
    else:
        return norm.cdf(zscore)

"""
Run an inferential test on a team's GA

@return probability
"""
def inferHockeyGAg(year, team, line, over):
    list = getStandardDeviation(year, team, 0)
    mean = list[1][0]
    sd = list[1][1]

    zscore = (line - mean)/sd
    if over == True:
        return 1 - norm.cdf(zscore)
    else:
        return norm.cdf(zscore)

