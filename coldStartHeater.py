import datetime, time, webbrowser
from selenium import webdriver
from dotenv import dotenv_values

config = dotenv_values(".env")
COLD_URL = config["COLD_URL"]
LOG_PATH = config["LOG_PATH"]

while True:
    timeOfRequest = datetime.datetime.now()
    try:
        browser = webdriver.Firefox()
        browser.get(COLD_URL)
        # TODO wait some amount of time
        # check something on the page with selenium. if it isn't there, raise exception.
        coldStartHeaterLog = open(
            LOG_PATH + "coldStartHeaterLog.txt",
            "a",
        )
        coldStartHeaterLog.write(
            timeOfRequest.strftime("%m/%d/%Y, %H:%M:%S")
            + "   Cold start successfully heated\n"
        )
        coldStartHeaterLog.close()
    except:
        coldStartHeaterLog = open(
            LOG_PATH + "coldStartHeaterLog.txt",
            "a",
        )
        coldStartHeaterLog.write(
            timeOfRequest.strftime("%m/%d/%Y, %H:%M:%S") + "   Something went wrong\n"
        )
        coldStartHeaterLog.close()
    time.sleep(810)
    browser.quit()
    time.sleep(30)
