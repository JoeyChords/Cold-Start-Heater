import datetime, logging, time, webbrowser
from selenium import webdriver
from dotenv import dotenv_values

config = dotenv_values(".env")
COLD_URL = config["COLD_URL"]
logging.basicConfig(filename="coldStartHeater.log", level=logging.INFO)
timeStarted = datetime.datetime.now()
logging.info(
    timeStarted.strftime("%m/%d/%Y, %H:%M:%S")
    + "   coldStartHeater started on "
    + COLD_URL
)

while True:
    timeOfRequest = datetime.datetime.now()
    try:
        browser = webdriver.Firefox()
        browser.get(COLD_URL)
        # TODO wait some amount of time
        # check something on the page with selenium. if it isn't there, raise exception.
        logging.info(
            timeOfRequest.strftime("%m/%d/%Y, %H:%M:%S")
            + "   Cold start at "
            + COLD_URL
            + " successfully heated"
        )
    except:
        logging.exception(
            timeOfRequest.strftime("%m/%d/%Y, %H:%M:%S") + "   Something went wrong"
        )
    time.sleep(810)
    browser.quit()
    time.sleep(30)
