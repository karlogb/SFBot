from dash import dcc
from dash import html
from dash.dependencies import Output, Input, State

from app import app
from Functions import globalVariables, AccountFun, SettingsFun, LogFun
from Utils import ComUtils, HTMLUtils, logUtil

cache = ""


def getLayout():
    global cache
    if cache == "":
        cache = [
            html.H2("Přehled účtů"),
            html.H3("Prověď akci na všech účtech"),
            html.Table(id="action_table", children=[
                html.Tr([
                    html.Td(html.Button('Přihlásit', id="bAccs_Perform_Login")),
                    html.Td(html.Button('Odhlásit', id="bAccs_Perform_Logout")),
                    html.Td(html.Button('Spustit', id="bAccs_Perform_Start")),
                    html.Td(html.Button('Vypnout', id="bAccs_Perform_Stop")),
                    html.Td(html.Button('Zrušit aktuální akci', id="bAccs_Perform_Cancel")),
                ])
            ]),
            html.H3("Vyber sloupce v tabulce"),
            dcc.Dropdown(options=getColums(), value=getColumDefaults(),
                         multi=True, id="iColumSelection"),
            html.Div(id='accounts_Overview', children=[]),
            dcc.Interval(id='accounts_interval',
                         interval=globalVariables.WEBSITE_REFRESH_RATE, n_intervals=0)
            ]
    return cache


def getColums():
    return[{'label': a["label"], 'value':a["value"]} for a in globalVariables.columNames]


def getColumDefaults():
    arr = []
    for a in globalVariables.columNames:
        if a["default"]:
            arr.append(a["value"])
    return arr


def initCallbacks():
    @app.callback(Output('AccsAction1', 'children'), [Input('bAccs_Perform_Login', 'n_clicks')])
    def cb_AccountsAction_Login(n):
        if n is None: 
            return []
        logUtil.log(2, "Performing !Login on All Accounts")
        for a in globalVariables.account_names:
            ComUtils.curlGet("bot/accounts/"+a+"!Login")
        logUtil.log(2, "All accounts should be logged in now")
        return []

    @app.callback(Output('AccsAction2', 'children'), [Input('bAccs_Perform_Logout', 'n_clicks')])
    def cb_AccountsAction_Logout(n):
        if n is None: 
            return []
        logUtil.log(2, "Performing !Logout on All Accounts")
        for a in globalVariables.account_names:
            ComUtils.curlGet("bot/accounts/"+a+"!Logout")
        logUtil.log(2, "All accounts should be logged out now")
        return []

    @app.callback(Output('AccsAction3', 'children'), [Input('bAccs_Perform_Start', 'n_clicks')])
    def cb_AccountsAction_Start(n):
        if n is None: 
            return []
        logUtil.log(2, "Performing !Start on All Accounts")
        for a in globalVariables.account_names:
            ComUtils.curlGet("bot/accounts/"+a+"!Start")
        logUtil.log(2, "All accounts should be started now")
        return []

    @app.callback(Output('AccsAction4', 'children'), [Input('bAccs_Perform_Stop', 'n_clicks')])
    def cb_AccountsAction_Stop(n):
        if n is None: 
            return []
        logUtil.log(2, "Performing !Stop on All Accounts")
        for a in globalVariables.account_names:
            ComUtils.curlGet("bot/accounts/"+a+"!Stop")
        logUtil.log(2, "All accounts should be stopped now")
        return []

    @app.callback(Output('AccsAction5', 'children'), [Input('bAccs_Perform_Cancel', 'n_clicks')])
    def cb_AccountsAction_Cancel(n):
        if n is None: 
            return []
        logUtil.log(2, "Performing !StopCurrentAction on All Accounts")
        for a in globalVariables.account_names:
            ComUtils.curlGet("bot/accounts/"+a+"!StopCurrentAction")
        logUtil.log(2, "All accounts should´ve stopped current action now")
        return []

    @app.callback(Output('accounts_Overview', 'children'),
                  [Input('accounts_interval', 'n_intervals')],
                  # [Input('bAccount', 'n_clicks')],
                  [State('iColumSelection', 'value')])
    def cb_Accounts(n, pSelect):
        return AccountFun.getAccounts(pSelect)
