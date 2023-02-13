import base64
import datetime
import io

import dash
from dash.dependencies import Input, Output, State
from dash import dcc, html, dash_table

import pandas as pd
import plotly.express as px

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div([
    html.Div([
        html.H1("Beta de analizador de datos Gama"),
        html.Img(src= "assets/tuqueque.png"),
    ],className="banner")
])

if __name__== ('__main__'):
    app.run_server(debug=True)

