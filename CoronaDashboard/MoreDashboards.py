from Dashboard import get_country_data
from pandas import read_csv
import numpy as np
import plotly.offline as pyo
import plotly.graph_objs as go
import dash
from dash import dcc
from dash import html
from dash import dependencies
data = read_csv('data.csv')





"""Building the app"""
# ---------------------------------------------------------------------------

# Initializing the app
app = dash.Dash(__name__)
server = app.server

# Building the app layout
app.layout = html.Div([
    html.H1("Corona Tracker DashBoard", style={"text-align": "center"}),
    html.Br(),
    html.Div(
                children=[
                    html.Label('Select Country'),
                    dcc.Dropdown(
                        id="selected_country",
                        options=list(data.iloc[:, 0]),
                        value="All"
                    ),
                ],
            ),
        dcc.Graph(id="countries_cases")
    ])

@app.callback(
    dependencies.Output("countries_cases", "figure"),
    [
    dependencies.Input("selected_country", "value")
    ]
)
def update_fig(selected_country):
    if selected_country != "All":
        country_data = data[data.iloc[:, 0] == selected_country]
        Total_cases = country_data['TotalCases']
        Total_deaths = country_data['TotalDeaths']
        New_cases = country_data['New Cases/1M pop']
        New_deaths = country_data['New Deaths/1M pop']
        TotalRecovered = country_data['TotalRecovered']
        print("#####################\n", Total_deaths, Total_cases)
        return {
        "data": [
            {
                'x': ['total cases', 'total deaths', 'New Cases/1M pop', 'New Deaths/1M pop', 'TotalRecovered'],
                "y": [float(Total_cases), float(Total_deaths), float(New_cases), float(New_deaths), float(TotalRecovered)],
                "type": "bar",
            },
        ],
        }

    else:
        country_data = data
    return {
        "data": [
            {
                "x": country_data['Unnamed: 0'],
                "y": country_data['TotalCases'],
                "type": "bar",
            },
        ],
        "layout": {
            "title": f"Top Movies by Rating",
            "xaxis": {"title": "Country"},
            "yaxis": {"title": "Cases"},
        },
    }


app.run_server(debug=True)

