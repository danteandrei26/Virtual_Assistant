from Virtual_Assistant_TestingEnv.Features.CryptoCoinSearcher.seleniumLocators import *
from Virtual_Assistant_TestingEnv.Features.generalWebMethods import *


# Update whatIKnowDictionary
class cryptoSearcher(webBrowser):
    def __init__(self):
        self.knownCommands = {"search coin": self.searchCoinAndReturnPrice}

    def updateKnowledge(self, baseDict):
        baseDict.update(self.knownCommands)
        return baseDict

    # Search coin
    def searchCoinAndReturnPrice(self, timeout=10):
        audio.speak("What coin do you want me to search for?")
        coin = audio.getAudio().lower()
        audio.speak(f"I'm searching for the price of {coin}")

        self.startBrowser()
        self.driver.get("https://dexscreener.com/")

        searchField = WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located((By.XPATH, searchField_Locator)))
        searchField.click()

        searchField = WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located((By.XPATH, searchField_Locator_child)))
        searchField.click()

        searchField.send_keys(coin)
        WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located((By.XPATH, dropDownMenuBox_Locator)))
        time.sleep(1.5)
        searchField.send_keys(Keys.RETURN)

        try:
            price = WebDriverWait(self.driver, 3).until(EC.presence_of_element_located((By.XPATH, coinPrice_Locator)))
            return f"I found that the price of {coin} is {price.text}", self.closeBrowser()
        except:
            return f"It seems that the coin {coin} doesn't exist", self.closeBrowser()





