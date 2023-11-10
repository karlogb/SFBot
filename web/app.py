import dash
import flask
from dash import dcc
from dash import html
from dash import dash_table as dt
import logging

from Functions import globalVariables
from Utils import logUtil

app = dash.Dash('auth')

def initServer():
    if globalVariables.debugLevel > 0:
        log = logging.getLogger('werkzeug')
        log.setLevel(logging.ERROR)
    server = app.server

    @server.route('/favicon.ico')
    def favicon():
        logUtil.log(1,"Favicon requested")
        return flask.redirect('https://www.mfbot.de/favicon.ico')

    app.config.external_stylesheets = ["https://safiron.eu/sources/dark-min.css"]
    #app.config['suppress_callback_exceptions'] = True

    app.layout = html.Div([
        html.Div([
        html.Link(rel="ikona", href="favicon.ico"),
        dcc.Location(id='url', refresh=False),
        #html.Table(html.Tr([html.Th(html.Img(id='image', src='https://www.mfbot.de/forum/styles/black/theme/images/logo.png')), html.Th(html.H1('MFBot Python Web Interface'))])),
        html.Table(html.Tr([
            html.Th(dcc.Link('Přehled účtů', href='/')),
            html.Th(dcc.Link('Detail účtu', href='/Account')),
            #html.Th(dcc.Link('Account Settings', href='/AccountSettings')),
            #html.Th(dcc.Link('Global Bot Log', href='/Bot_Log')),
            #html.Th(dcc.Link('Global Bot Settings', href='/Settings')),
            ]), id='navigation')], id="header"),

        html.Div(id='page_content'),
        html.Div(children=[
            # needed for JS load
            dcc.Graph(id='jsLoad', style={'display': 'none'}),
            html.Div(dt.DataTable(), style={'display': 'none'}),
            html.Div(id='sliderRadio'),
            html.Div(id='AccAction'),
            html.Div(id='AccsAction1'),
            html.Div(id='AccsAction2'),
            html.Div(id='AccsAction3'),
            html.Div(id='AccsAction4'),
            html.Div(id='AccsAction5'),
            ])
    ])