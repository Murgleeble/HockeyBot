INFORMATION AND SET UP REQUIRED TO USE HOCKEYBOT:

PURPOSE:
    This project started about the time I began sportsbetting.  I would spend hours pouring over data, performing inferential
    tests by hand in order to find the best plays each day.  I decided to write code that would save me the effort, and this project
    is the culmination of about a year's worth of work.  Currently, the project only finds ideal NHL "shots on goal" over/unders,
    using PrizePicks.com as a reference site; I do plan on expanding it to basketball stats in the future.  Although I do NOT guarantee
    profit from using this model, I have made a significant enough amount of profit over a long enough period of time that I feel 
    safe continuing to use the model (i.e., I feel that my success using this is not simply due to luck).  Beyond personal profit,
    the project served as a chance for me to improve my skills as a programmer.  Since its inception, I have learned how to format json,
    navigate APIs, use webdrivers and webscrapers, and perform inferential statistical analysis using a computer.  I am very proud of what
    this project has become.
    (Updated on 2/9/2023, public version 1.0)

SET UP:
    1: In the directory into which you have placed the folder 'HockeyBot' and it's contents:
        -Create a folder in that directory named 'graphs'.  This will saved all performance histograms made.

        -Create another folder in that directory called 'dataS' with subdirectory: 'dataS/hockey/22-23'
            (and under 'hockey', any seasonal folders matching the same format if used after 22-23)
         This will save all player data in a .csv format

        -download the chrome webdriver and place chromedriver (unix exec file) in the same directory as 'HockeyBot'
            (view https://www.selenium.dev/downloads/ in order to find a compatabile version)
    
    2: In each file within the folder 'HockeyBot', reassign the variable 'masterPath' to whatever the path to the
       directory is.  For example: 'Users/harborwolff/desktop' (DO NOT add a trailing '/')
    
    3: Make sure python is installed on your computer, as well as the libraries:
        -json
        -requests  
        -os
        -math
        -scipy.stats
        -selenium (view selenium.dev in order to find correct version)
        -colorama
        -matplotlib
        -time

    4: Run 'idCreator.py' once (and then again whenever you wish to update the current list of active players' ids)

    5: You should now be set to run the program.  Invocation: '{PATH} python3 main'

FILE DESCRIPTIONS:

defunct programs:
    Old files used in very early prototypes of HockeyBot.  Not relevant to the project anymore, but useful to see the
    evolution of the project

jsons:
    a few json files used to store information on teams, players, and daily lines.  Also includes a few '.txt's that 
    breakdown a few json formats

idCreator.py:
    should only be invoked every now and then to update the list of active NHLer's IDs (in the NHLAPI)

inferential.py:
    uses NHLAPI to gather lists of data on NHLers and stores them in '.csv's in dataS.  The mathematical backbone of the program

lineJudge.py:
    uses inferential's results to make inferential z-score assessments of player performance in order to predict future performances

webdriver.py:
    uses selenium to scrape data off of PrizePicks.com.  Also outputs the time it takes to do each task (around 22 seconds)

nhlAPI.py:
    uses webdriver.py to get the daily player lines off of PrizePicks.com and update:
        -dailyLines.json
        -each player's .csv file of stats

runAll.py:
    given an up-to-date 'dailyLines.json', performs both inferential z-score tests on mean player performance and also a simple 
    percentage calulation, outputting each to the terminal with coloration to easily spot the best value players

main:
    updates dailyLines and player stats, then runs runAll.  

visuals.py:
    uses matplotlib to create a simple histogram of a requested player given a certain stats line.  not necessary for functionality,
    but I like it to better visualize lines.

Update Log:
v2.0.0:
    -Added additional error handling
    -fixed an issue in idCreator (didn't previously build Kraken players)
