from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Virtual_Assistant_TestingEnv.Functions.audioInAndOut import audioInAndOut
import time

PATH = "D:\Python_3.6.7_Projects\Virtual_Assistant\chromedriver.exe"
audio = audioInAndOut()
class webBrowser:
    def __init__(self):
        self.knownCommands = {"start browser": self.startBrowser, "close browser": self.closeBrowser}

    def updateKnowledge(self, baseDict):
        baseDict.update(self.knownCommands)
        return baseDict

    def startBrowser(self):
        self.driver = webdriver.Chrome(PATH)
        self.driver.maximize_window()
        self.driver.refresh()
        return "Browser is now open"

    def closeBrowser(self):
        try:
            self.driver.quit()
            return "I've closed it"
        except:
            return "Browser isn't opened"





