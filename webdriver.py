"""
Webdriver uses the Selenium webdriver to scrape the daily lines from Prizepicks.com and update the dailyLines.json file
"""
masterPath = '/Users/harborwolff/desktop'
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time
import os
import json

def getLines():
    """ The Webdriving... Gets the daily lines """
    #setup
    options = webdriver.ChromeOptions()
    options.headless = True

    user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36'
    options.add_argument('user-agent={0}'.format(user_agent))

    prefs = {"profile.managed_default_content_settings.images": 2}
    options.add_experimental_option("prefs", prefs)

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

    PATH = f"{masterPath}/chromedriver.exe"

    startTime = time.time()
    print("Beginning PrizePicks scrape\n")
    #Runtime
    driver.get("https://app.prizepicks.com/")

    quit = driver.find_element(by=By.CLASS_NAME, value="close")
    quit.click()

    #find leeg
    league = driver.find_element(By.XPATH, "//*[text()='NHL']")
    league.click()

    #find claz
    stat = driver.find_element(By.XPATH, "//*[text()='Shots On Goal']")
    stat.click()

    names = driver.find_elements(By.CLASS_NAME, value="name")
    names.reverse()

    statistics = driver.find_elements(By.CLASS_NAME, value="score")
    statistics.reverse()

    compTime = time.time()
    print(compTime - startTime)
    print("Compiling data\n")
    finalList = []
    for i in range(0, len(statistics)):
        finalList.append({"name" : names[i].text.split(" ")[0] + " " + names[i].text.split(" ")[1], "shots" : statistics[i].text})
    driver.quit()

    writeTime = time.time()
    print(writeTime - startTime)
    os.remove(f"{masterPath}/project/jsons/dailyLines.json")
    with open(f"{masterPath}/project/jsons/dailyLines.json", 'w') as fp:
        fp.write(json.dumps(finalList, indent=1))
        pass
