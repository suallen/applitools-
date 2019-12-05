from selenium import webdriver
from applitools.selenium.eyes import Eyes
import csv
from applitools.eyes import MatchLevel
from applitools.selenium.eyes import StitchMode


class Pso:

    eyes = Eyes()

    # Initialize the eyes SDK and set your private API key.
    eyes.api_key = '<ENTER YOUR APPLITOOL EYES API KEY>'
    eyes.force_full_page_screenshot = True
    #eyes.match_level = MatchLevel.CONTENT
    eyes.stitch_mode = StitchMode.CSS
    #eyes.match_level = MatchLevel.LAYOUT

    browsers = ["Chrome", "Firefox", "Edge"]
    for browser in browsers:
        if (browser == "Chrome"):
            driver = webdriver.Chrome(r'C:\Users\admin\PycharmProjects\suallen-2019-practice\chromedriver\chromedriver.exe')
            eyes.open(driver, "Stelara!", "Chrome Test", {'width': 1366, 'height': 768})
            #driver.maximize_window()
        elif (browser == "Firefox"):
            driver = webdriver.Firefox(executable_path=r'.\\geckodriver.exe')
            eyes.open(driver, "Stelara!", "Firefox Test", {'width': 1366, 'height': 768})
            #driver.maximize_window()
        elif (browser == "Edge"):
            driver = webdriver.Edge(r'C:\Users\admin\PycharmProjects\suallen-2019-practice\microsoftWebDriver\MicrosoftWebDriver.exe')
            eyes.open(driver, "Stelara!", "Edge Test", {'width': 1366, 'height': 768})
            #driver.maximize_window()

        try:

            with open(r'C:\Users\admin\PycharmProjects\suallen-2019-practice\plaque-psoriasis.csv', 'r+') as f:
                data = csv.reader(f)
                for row in data:
                    page_name = str(row[0])
                    base_url = 'https://www.stelarainfo.com/'
                    #base_url = 'https://<USERNAME>:<PASSWORD>@<URL>' //if there is a basic auth
                    url = base_url + page_name
                    driver.get(url)
                    eyes.check_window(page_name)


            eyes.close()

        finally:

            driver.quit()
            eyes.abort_if_not_closed()