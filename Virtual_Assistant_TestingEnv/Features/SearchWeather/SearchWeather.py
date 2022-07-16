from Virtual_Assistant_TestingEnv.Features.SearchWeather.seleniumLocators import *
from Virtual_Assistant_TestingEnv.Features.generalWebMethods import *


# Update whatIKnowDictionary
class SearcherWeather(webBrowser):
    def __init__(self):
        self.knownCommands = {"weather": "I'm searching right now!"}

    def updateKnowledge(self, baseDict):
        baseDict.update(self.knownCommands)
        return baseDict

    # Search weather
    def searchWeather(self, timeout=10):
        self.startBrowser()
        self.driver.get(pathToTheGoogle)

        cookiesBox = WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located((By.XPATH, cookiesBoxLocator)))
        cookiesBox.click()

        searchBox = WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located((By.XPATH, searchBoxLocator)))
        searchBox.click()
        searchBox.send_keys("weather")
        searchBox.submit()

        temperatureBox = WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located((By.XPATH, temperatureBoxLocator)))
        temperatureBox.click()

        statusBox = WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located((By.XPATH, statusBoxLocator)))
        statusBox.click()

        weather = f"The temperature is about {temperatureBox.text}°C, the weather is most likely {statusBox.text}"
        return weather
