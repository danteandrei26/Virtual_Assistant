from Virtual_Assistant_TestingEnv.Features.Google.seleniumLocators import *
from Virtual_Assistant_TestingEnv.Features.generalWebMethods import *

# Google search Feature
class google(webBrowser):
    def __init__(self):
        self.knownCommands = {"google": self.searchOnGoogle}

    def updateKnowledge(self, baseDict):
        baseDict.update(self.knownCommands)
        return baseDict

    def goToGoogle(self, timeout=10):
        try:
            body = self.driver.find_element_by_tag_name("body")
            body.send_keys(Keys.CONTROL + 't')
        except:
            self.startBrowser()
        self.driver.get("https://google.com/")
        acceptAllButton = WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located((By.XPATH, acceeptAll_Locator)))
        acceptAllButton.click()


    def searchOnGoogle(self, timeout=10):
        self.goToGoogle()
        searchField = WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located((By.XPATH, inputFieldGoogle_Locator)))
        searchField.click()
        audio.speak("What do you want me to search?")
        toSearch = audio.getAudio().lower()
        searchField.send_keys(toSearch)
        searchField.send_keys(Keys.RETURN)
        return f"I've searched {toSearch} on google and I've found this"


