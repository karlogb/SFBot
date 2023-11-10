from datetime import datetime, timedelta


def init():
    global VALID_USERNAME_PASSWORD_WEB_INTERFACE, USERNAME, PASSWORD, ADRESS, serverPort, REFRESH_RATE_ALL_DATA, WEBSITE_REFRESH_RATE
    global settings, ACCOUNTS_o, SETTING_LIST, ACC_SETTING_LIST, settings_send, account_Setting_Send, LIGHT, settingsChanges, logs, accounts, account_names
    global callbackList, CACHE_ACCS, GLOBAL_SETTINGS_lastRequest, CACHE_BOT_LOG, accLast, noSlider, accountOptions, columNames, columHeaders
    global debugLevel, debugLevels, debugColors
    VALID_USERNAME_PASSWORD_WEB_INTERFACE = [
        ['Entwickler', 'MFBot5.0'],
        ['Kaja', 'Chad']
    ]
    USERNAME = "MFBotAdmin"
    PASSWORD = "MFBotAdminPassword"
    ADRESS = 'http://192.168.1.65:4235/'
    serverPort = 4335

    # Time in s after wich new Data should be requested from Remote Interface
    REFRESH_RATE_ALL_DATA = 5
    # Time in ms after wich the website shall request new Data
    WEBSITE_REFRESH_RATE = 10*1000

    LIGHT = False
    settings = {}
    ACCOUNTS_o = {}
    SETTING_LIST = []
    ACC_SETTING_LIST = []
    settings_send = {}
    account_Setting_Send = {}
    settingsChanges = False
    logs = []
    accounts = []
    account_names = []
    callbackList = []

    CACHE_ACCS = {"lastRequest": datetime.now() - timedelta(minutes=15),
                  "data": [], "newData": True}
    GLOBAL_SETTINGS_lastRequest = datetime.now() - timedelta(minutes=15)
    CACHE_BOT_LOG = {"lastRequest": datetime.now() - timedelta(minutes=15),
                     "data": [], "newData": True, "amount": 25, "maxTime": datetime.now()}

    accLast = ""
    noSlider = False
    accountOptions = [
        {'label': 'Přihlásit', 'value': '!Login'},
        {'label': 'Odhlásit', 'value': '!Logout'},
        {'label': 'Zapnout', 'value': '!Start'},
        {'label': 'Vypnout', 'value': '!Stop'},
        {'label': 'Přestat provádět akci', 'value': '!StopCurrentAction'}
        ]
    columNames = [
        {'label': 'Přihlášen?', 'value': 'isLoggedIn', 'default': True, 'type': ''},
        {'label': 'Spuštěn?', 'value': 'isStarted', 'default': True, 'type': ''},
        {'label': 'Aktuální akce', 'value': 'currentAction', 'default': True, 'type': ''},
        {'label': 'Zaneprázdněn do', 'value': 'busyUntil', 'default': True, 'type': 'time'},
        {'label': 'Pivo', 'value': 'usedBeer', 'default': False, 'type': 'beer'},
        {'label': 'Level', 'value': 'level', 'default': True, 'type': ''},
        {'label': 'XP %', 'value': 'experienceInPercent', 'default': True, 'type': 'percent'},
        {'label': 'Cech', 'value': 'guildName', 'default': False, 'type': ''},
        {'label': 'Třída', 'value': 'class', 'default': True, 'type': ''},
        {'label': 'Zlato', 'value': 'gold', 'default': True, 'type': ''},
        {'label': 'Houbičky', 'value': 'mushrooms', 'default': True, 'type': ''},
        {'label': 'Touha', 'value': 'aLU', 'default': True, 'type': ''},
        {'label': 'Portál?', 'value': 'portalFought', 'default': False, 'type': ''},
        {'label': 'Časovač podzemí', 'value': 'dungeonTimer', 'default': False, 'type': 'time'},
        {'label': 'Věhlas', 'value': 'honor', 'default': False, 'type': ''},
        {'label': 'Rank', 'value': 'rank', 'default': False, 'type': ''},
        {'label': 'XP', 'value': 'experience', 'default': False, 'type': ''},
        {'label': 'XP Potřeba', 'value': 'experienceForNextLevel', 'default': False, 'type': ''},
        {'label': 'Rychlost mazlíčka', 'value': 'mountSpeed', 'default': False, 'type': ''},
        {'label': 'Mazlíček do', 'value': 'mountEnd', 'default': False, 'type': 'time'},
        {'label': 'Zrcadlo?', 'value': 'hasMirror', 'default': False, 'type': ''},
        {'label': 'Počet střepů', 'value': 'mirrorProgress', 'default': False, 'type': ''},
        {'label': 'SA %', 'value': 'albumProgress', 'default': False, 'type': 'percent'},
        {'label': 'Arena XP', 'value': 'arenaXP', 'default': False, 'type': ''},
        {'label': 'Aura', 'value': 'aura', 'default': False, 'type': ''}
    ]
    columHeaders = {}
    for a in columNames:
        columHeaders[a["value"]] = {'label': a["label"], 'type': a["type"]}
    debugLevel = 3
    debugLevels = ["Special Debug","Debug","Info","Warnings","Errors"]
    debugColors = ['\033[34m','\033[90m','\033[32m','\033[33;1m','\033[31m']
