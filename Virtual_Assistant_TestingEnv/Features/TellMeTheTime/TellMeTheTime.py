import datetime

class TheTime():
    def __init__(self):
        self.knownCommands = {"Tell Me The Time": ""}

    def updateKnowledge(self, baseDict):
        baseDict.update(self.knownCommands)
        return baseDict

    # Search weather
    def TellMeTheTime(self):
        self.theTime = datetime.datetime.now().strftime("%H:%M")
        theTimeIs = f"the time is {self.theTime}"
        return theTimeIs


