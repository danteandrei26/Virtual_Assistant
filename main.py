# Import basic commands
from Virtual_Assistant_TestingEnv.Functions.baseKnowledge import baseKnowledgeClass

# Import modular commands
from Virtual_Assistant_TestingEnv.Features.CryptoCoinSearcher.cryptoCoinSearcher import cryptoSearcher
from Virtual_Assistant_TestingEnv.Features.Google.google import google
from Virtual_Assistant_TestingEnv.Features.SearchWeather.SearchWeather import SearcherWeather
from Virtual_Assistant_TestingEnv.Features.TellMeTheTime.TellMeTheTime import TheTime


# Import base functions
from Virtual_Assistant_TestingEnv.Features.generalWebMethods import webBrowser
from Virtual_Assistant_TestingEnv.Functions.audioInAndOut import *

class protocol_0(Exception):
    """
    Protocol 0 - Emergency quit
    """
    pass


CoinSearch, Google, Weather, Time, webBrowser = cryptoSearcher(), google(), SearcherWeather(), TheTime(), webBrowser()

listOfModules = [CoinSearch, Google, Weather, Time, webBrowser]

def importModulesKnowledge(listOfModules):
    """
    This method imports all the modules commands
    :return: baseCommands - dictionary with all commands.
    """
    baseCommands = baseKnowledgeClass().baseCommands

    for module in listOfModules:
        baseCommands.update(module.updateKnowledge(baseCommands))
    return baseCommands


def interpretAudio(text):
    if type(text) is not None:
        for key in allCommandsDict.keys():
            if key in text:
                try:
                    audio.speak(allCommandsDict[key])
                except:
                    text = allCommandsDict[key]()
                    if text:
                        audio.speak(text)

    if "execute protocol 0" in text:
        audio.speak("Protocol 0 executed")
        raise protocol_0


# Main loop:
def mainLoop():
    """
    This method is used to start the app
    :return:
    """
    global allCommandsDict
    allCommandsDict = importModulesKnowledge(listOfModules)
    global audio
    audio = audioInAndOut()
    audio.speak("I am ready!")
    print(allCommandsDict)
    for x in range(0, 50):
        try:
            timeBefore = time.time()
            print(f"Listening.. {x}")
            text = audio.getAudio().lower()
            interpretAudio(text)

            timeAfter = time.time()
            timeElapsed = timeAfter - timeBefore
            print(f"Time elapsed: {timeElapsed}")
        except protocol_0:
            return

mainLoop()
