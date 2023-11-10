from datetime import datetime, timedelta
from Functions import globalVariables
import colorama
colorama.init()

def log(pLevel, pMessage):
    if pLevel >= globalVariables.debugLevel:
        text = (str(datetime.now()) + " [" +
            globalVariables.debugLevels[pLevel] +
            "]: " + str(pMessage))
        open("log.txt","a").write(text + "\n")
        print(globalVariables.debugColors[pLevel] + text + '\033[0m')
