import os
import json
import dash
import dash_core_components as dcc
import plotly.express as px
import dash_html_components as html
import pandas as pd
from dash.dependencies import Output, Input
import dash_bootstrap_components as dbc

PLOTLY_LOGO = "https://images.plot.ly/logo/new-branding/plotly-logomark.png"
FEMALE_COLOR = "rgb(239, 85, 59)"
app = dash.Dash(__name__,
                external_stylesheets=[dbc.themes.BOOTSTRAP], suppress_callback_exceptions=True)
# styling the sidebar
SIDEBAR_STYLE = {
    "position": "fixed",
    "top": 0,
    "left": 0,
    "bottom": 0,
    "width": "16rem",
    "padding": "2rem 1rem",
    "background-color": "#f8f9fa",
}

# padding for the page content
CONTENT_STYLE = {
    "margin-left": "2rem",
    "margin-right": "2rem",
    "padding": "2rem 1rem",
}

races_name = []
data = {}
for filename in os.listdir("data"):
    # print(filename)
    with open(f"data/{filename}", 'r', encoding="utf8") as f:
        obj = json.load(f)
        race_name = os.path.splitext(filename)[0][7:-1]
        # print(race_name)
        races_name.append(race_name)
        data[race_name] = pd.DataFrame(obj["classification"])
        data[race_name]['chipTime hh:mm'] = [dat[0:5]
                                             for dat in data[race_name]['chipTime']]
        # data[race_name]['chipTimePy'] = data[race_name]['chipTime'].dt.to_pydatetime()
        # .reset_index(drop=True)
        data[race_name].sort_values("chipTimeInSec", inplace=True)
        if "gender" in data[race_name]:
            data[race_name]["gender"] = ["M" if dat == 1 else "F" if dat
                                         == 2 else "Not Specified" for dat in data[race_name]["gender"]]
        elif "category" in data[race_name]:
            data[race_name]["gender"] = ["M" if dat[0:1] == "男" else "F" if dat[0:1]
                                         == "女" else "Not Specified" for dat in data[race_name]["category"]]
        if "HALF MARATHON" in race_name:
            data[race_name]["7kmTime"] = [dat[0]["cumulativeTime"][0:5]
                                          for dat in data[race_name]["splits"]]
            data[race_name]["9kmTime"] = [dat[1]["cumulativeTime"][0:5]
                                          for dat in data[race_name]["splits"]]
            data[race_name]["14kmTime"] = [dat[2]["cumulativeTime"][0:5]
                                           for dat in data[race_name]["splits"]]
            data[race_name]["19kmTime"] = [dat[3]["cumulativeTime"][0:5]
                                           for dat in data[race_name]["splits"]]
        elif "MARATHON" in race_name:
            data[race_name]["10kmTime"] = [dat[0]["cumulativeTime"][0:5]
                                           for dat in data[race_name]["splits"]]
            data[race_name]["15kmTime"] = [dat[1]["cumulativeTime"][0:5]
                                           for dat in data[race_name]["splits"]]
            data[race_name]["20kmTime"] = [dat[3]["cumulativeTime"][0:5]
                                           for dat in data[race_name]["splits"]]
            data[race_name]["HalfWayTime"] = [dat[4]["cumulativeTime"][0:5]
                                              for dat in data[race_name]["splits"]]
            data[race_name]["25kmTime"] = [dat[5]["cumulativeTime"][0:5]
                                           for dat in data[race_name]["splits"]]
            data[race_name]["30kmTime"] = [dat[6]["cumulativeTime"][0:5]
                                           for dat in data[race_name]["splits"]]
            data[race_name]["35kmTime"] = [dat[7]["cumulativeTime"][0:5]
                                           for dat in data[race_name]["splits"]]
            data[race_name]["40kmTime"] = [dat[8]["cumulativeTime"][0:5]
                                           for dat in data[race_name]["splits"]]
# category_10k_elite = data["10KM ELITE"]["category"].str[0:1]
# print(category_10k_elite.head())
# gender_10k_elite = "M" if category_10k_elite == "男" else "F" if category_10k_elite == "女" else "Not Specified"
# data["10KM ELITE"]["gender"] = ["M" if dat[0:1] == "男" else "F" if dat[0:1]
#                                 == "女" else "Not Specified" for dat in data["10KM ELITE"]["category"]]

# @app.callback(
#     Output
# )

header = html.Div(
    [
        html.H1(children="HK Marathon 2021 Analytics",),
        html.P(
            children="Displaying the result of Standard Chartered Hong Kong Marathon 2021",
        ),
    ]
)

navbar = dbc.Navbar(
    [
        dbc.Container(
            [
                html.Div(
                    # Use row and col to control vertical alignment of logo / brand
                    dbc.Row(
                        [
                            dbc.Col(
                                html.A(
                                    [
                                        html.Img(src=PLOTLY_LOGO,
                                                 height="30px")
                                    ], href="https://plotly.com"
                                )
                            ),
                            dbc.Col(dbc.NavbarBrand(
                                "HK Marathon 2021 Data Analytics", className="ms-2")),
                        ],
                        align="center",
                        className="g-0",
                    ),
                    style={"textDecoration": "none"},
                ),
                dbc.Nav(
                    [
                        dbc.NavLink("Home", href="/", active="exact"),
                        dbc.NavLink("10K", href="/10k", active="exact"),
                        dbc.NavLink("Half-Marathon",
                                    href="/half-marathon", active="exact"),
                        dbc.NavLink("Marathon", href="/marathon",
                                    active="exact"),
                    ],
                    pills=True
                )
            ]
        ),
    ],
    color="dark",
    dark=True,
    # style=SIDEBAR_STYLE
)

content = html.Div(
    [
        html.Div(id="page-content", children=[], style=CONTENT_STYLE)
    ]
)


layout_index = html.Div(
    children=[
        html.H1(children="HK Marathon 2021 Analytics",),
        html.P(
            [
                "A data analytic website of Standard Chartered Hong Kong Marathon 2021 using ",
                html.A(
                    "Dash", href="https://dash.plotly.com/"
                ),
                "."
            ]
        ),
        html.P(
            [
                html.A(
                    "Data source", href="https://results.sporthive.com/events/6842055555920915712"
                )
            ]
        )],
    style={
        "font-size": 25
    }
)

# def chipSecToTime

# 10k fig
# print(data["10KM RUN1"].head())
figure_10k_run1 = px.histogram(
    data["10KM RUN1"], x='chipTime hh:mm', labels={"chipTime hh:mm": "Chip Time"}, title=f"10KM RUN1")
total_10k_run1 = data["10KM RUN1"].shape[0]
figure_10k_run2 = px.histogram(
    data["10KM RUN2"], x='chipTime hh:mm', labels={"chipTime hh:mm": "Chip Time"}, title="10KM RUN2")
total_10k_run2 = data["10KM RUN2"].shape[0]
figure_10k_run3 = px.histogram(
    data["10KM RUN3"], x='chipTime hh:mm', labels={"chipTime hh:mm": "Chip Time"}, title="10KM RUN3")
total_10k_run3 = data["10KM RUN3"].shape[0]
figure_10k_run4 = px.histogram(
    data["10KM RUN4"], x='chipTime hh:mm', labels={"chipTime hh:mm": "Chip Time"}, title="10KM RUN4")
total_10k_run4 = data["10KM RUN4"].shape[0]

layout_10k = html.Div(
    children=[
        dbc.Card(
            [
                dbc.CardHeader("10K ELITE"),
                dbc.CardBody([
                    dbc.RadioItems(
                        id="10k-elite-gender-filter",
                        options=[
                            {'label': 'All', 'value': 'All'},
                            {'label': 'All (Compare)', 'value': 'C'},
                            {'label': 'Male', 'value': 'M'},
                            {'label': 'Female', 'value': 'F'}
                        ],
                        value='All',
                        inline=True
                    ),
                    dcc.Graph(
                        id="10k-elite-chart"
                    ),
                    html.Div(id="10k-elite-total")

                ])
            ]
        ),
        html.Hr(),
        dbc.Card(
            [
                dbc.CardHeader("10KM RUN1"),
                dbc.CardBody([
                    dcc.Graph(
                        figure=figure_10k_run1
                    ),
                    html.Div(f"Total: {total_10k_run1}")
                ])
            ]
        ),
        html.Hr(),
        dbc.Card(
            [
                dbc.CardHeader("10KM RUN2"),
                dbc.CardBody([
                    dcc.Graph(
                        figure=figure_10k_run2
                    ),
                    html.Div(f"Total: {total_10k_run2}")
                ])
            ]
        ),
        html.Hr(),
        dbc.Card(
            [
                dbc.CardHeader("10KM RUN3"),
                dbc.CardBody([
                    dcc.Graph(
                        figure=figure_10k_run3
                    ),
                    html.Div(f"Total: {total_10k_run3}")
                ])
            ]
        ),
        html.Hr(),
        dbc.Card(
            [
                dbc.CardHeader("10KM RUN4"),
                dbc.CardBody([
                    dcc.Graph(
                        figure=figure_10k_run4
                    ),
                    html.Div(f"Total: {total_10k_run4}")
                ])
            ]
        ),
    ]
)

# fig half_marathon
print(type(data["HALF MARATHON ELITE"]["splits"][0]))
print(data["HALF MARATHON ELITE"]["7kmTime"].tail())

layout_half_marathon = html.Div(
    children=[
        dbc.Card(
            [
                dbc.CardHeader("HALF MARATHON ELITE"),
                dbc.CardBody([
                    dbc.RadioItems(
                        id="half-marathon-elite-gender-filter",
                        options=[
                            {'label': 'All', 'value': 'All'},
                            {'label': 'All (Compare)', 'value': 'C'},
                            {'label': 'Male', 'value': 'M'},
                            {'label': 'Female', 'value': 'F'}
                        ],
                        value='All',
                        inline=True
                    ),
                    dbc.RadioItems(
                        id="half-marathon-elite-distance-filter",
                        options=[
                            {'label': '7km', 'value': '7km'},
                            {'label': '9km', 'value': '9km'},
                            {'label': '14km', 'value': '14km'},
                            {'label': '19km', 'value': '19km'},
                            {'label': 'Finish', 'value': 'Finish'}
                        ],
                        value='Finish',
                        inline=True
                    ),
                    dcc.Graph(
                        id="half-marathon-elite-chart"
                    ),
                    html.Div(id="half-marathon-elite-total")

                ])
            ]
        ),
        html.Hr(),
        dbc.Card(
            [
                dbc.CardHeader("HALF MARATHON RUN1"),
                dbc.CardBody([
                    dbc.RadioItems(
                        id="half-marathon-run1-gender-filter",
                        options=[
                            {'label': 'All', 'value': 'All'},
                            {'label': 'All (Compare)', 'value': 'C'},
                            {'label': 'Male', 'value': 'M'},
                            {'label': 'Female', 'value': 'F'}
                        ],
                        value='All',
                        inline=True
                    ),
                    dbc.RadioItems(
                        id="half-marathon-run1-distance-filter",
                        options=[
                            {'label': '7km', 'value': '7km'},
                            {'label': '9km', 'value': '9km'},
                            {'label': '14km', 'value': '14km'},
                            {'label': '19km', 'value': '19km'},
                            {'label': 'Finish', 'value': 'Finish'}
                        ],
                        value='Finish',
                        inline=True
                    ),
                    dcc.Graph(
                        id="half-marathon-run1-chart"
                    ),
                    html.Div(id="half-marathon-run1-total")

                ])
            ]
        ),
        html.Hr(),
        dbc.Card(
            [
                dbc.CardHeader("HALF MARATHON RUN2"),
                dbc.CardBody([
                    dbc.RadioItems(
                        id="half-marathon-run2-gender-filter",
                        options=[
                            {'label': 'All', 'value': 'All'},
                            {'label': 'All (Compare)', 'value': 'C'},
                            {'label': 'Male', 'value': 'M'},
                            {'label': 'Female', 'value': 'F'}
                        ],
                        value='All',
                        inline=True
                    ),
                    dbc.RadioItems(
                        id="half-marathon-run2-distance-filter",
                        options=[
                            {'label': '7km', 'value': '7km'},
                            {'label': '9km', 'value': '9km'},
                            {'label': '14km', 'value': '14km'},
                            {'label': '19km', 'value': '19km'},
                            {'label': 'Finish', 'value': 'Finish'}
                        ],
                        value='Finish',
                        inline=True
                    ),
                    dcc.Graph(
                        id="half-marathon-run2-chart"
                    ),
                    html.Div(id="half-marathon-run2-total")

                ])
            ]
        ),
        html.Hr(),
        dbc.Card(
            [
                dbc.CardHeader("HALF MARATHON RUN3"),
                dbc.CardBody([
                    dbc.RadioItems(
                        id="half-marathon-run3-gender-filter",
                        options=[
                            {'label': 'All', 'value': 'All'},
                            {'label': 'All (Compare)', 'value': 'C'},
                            {'label': 'Male', 'value': 'M'},
                            {'label': 'Female', 'value': 'F'}
                        ],
                        value='All',
                        inline=True
                    ),
                    dbc.RadioItems(
                        id="half-marathon-run3-distance-filter",
                        options=[
                            {'label': '7km', 'value': '7km'},
                            {'label': '9km', 'value': '9km'},
                            {'label': '14km', 'value': '14km'},
                            {'label': '19km', 'value': '19km'},
                            {'label': 'Finish', 'value': 'Finish'}
                        ],
                        value='Finish',
                        inline=True
                    ),
                    dcc.Graph(
                        id="half-marathon-run3-chart"
                    ),
                    html.Div(id="half-marathon-run3-total")

                ])
            ]
        ),
    ]
)

layout_marathon = html.Div(
    [
        dbc.Card(
            [
                dbc.CardHeader("MARATHON ELITE"),
                dbc.CardBody([
                    dbc.RadioItems(
                        id="marathon-elite-gender-filter",
                        options=[
                            {'label': 'All', 'value': 'All'},
                            {'label': 'All (Compare)', 'value': 'C'},
                            {'label': 'Male', 'value': 'M'},
                            {'label': 'Female', 'value': 'F'}
                        ],
                        value='All',
                        inline=True
                    ),
                    dbc.RadioItems(
                        id="marathon-elite-distance-filter",
                        options=[
                            {'label': '10km', 'value': '10km'},
                            {'label': '15km', 'value': '15km'},
                            {'label': '20km', 'value': '20km'},
                            {'label': 'Half', 'value': 'Half'},
                            {'label': '25km', 'value': '25km'},
                            {'label': '30km', 'value': '30km'},
                            {'label': '35km', 'value': '35km'},
                            {'label': '40km', 'value': '40km'},
                            {'label': 'Finish', 'value': 'Finish'}
                        ],
                        value='Finish',
                        inline=True
                    ),
                    dcc.Graph(
                        id="marathon-elite-chart"
                    ),
                    html.Div(id="marathon-elite-total")

                ])
            ]
        ),
        html.Hr(),
        dbc.Card(
            [
                dbc.CardHeader("MARATHON RUN1"),
                dbc.CardBody([
                    dbc.RadioItems(
                        id="marathon-run1-gender-filter",
                        options=[
                            {'label': 'All', 'value': 'All'},
                            {'label': 'All (Compare)', 'value': 'C'},
                            {'label': 'Male', 'value': 'M'},
                            {'label': 'Female', 'value': 'F'}
                        ],
                        value='All',
                        inline=True
                    ),
                    dbc.RadioItems(
                        id="marathon-run1-distance-filter",
                        options=[
                            {'label': '10km', 'value': '10km'},
                            {'label': '15km', 'value': '15km'},
                            {'label': '20km', 'value': '20km'},
                            {'label': 'Half', 'value': 'Half'},
                            {'label': '25km', 'value': '25km'},
                            {'label': '30km', 'value': '30km'},
                            {'label': '35km', 'value': '35km'},
                            {'label': '40km', 'value': '40km'},
                            {'label': 'Finish', 'value': 'Finish'}
                        ],
                        value='Finish',
                        inline=True
                    ),
                    dcc.Graph(
                        id="marathon-run1-chart"
                    ),
                    html.Div(id="marathon-run1-total")

                ])
            ]
        ),
        html.Hr(),
        dbc.Card(
            [
                dbc.CardHeader("MARATHON RUN2"),
                dbc.CardBody([
                    dbc.RadioItems(
                        id="marathon-run2-gender-filter",
                        options=[
                            {'label': 'All', 'value': 'All'},
                            {'label': 'All (Compare)', 'value': 'C'},
                            {'label': 'Male', 'value': 'M'},
                            {'label': 'Female', 'value': 'F'}
                        ],
                        value='All',
                        inline=True
                    ),
                    dbc.RadioItems(
                        id="marathon-run2-distance-filter",
                        options=[
                            {'label': '10km', 'value': '10km'},
                            {'label': '15km', 'value': '15km'},
                            {'label': '20km', 'value': '20km'},
                            {'label': 'Half', 'value': 'Half'},
                            {'label': '25km', 'value': '25km'},
                            {'label': '30km', 'value': '30km'},
                            {'label': '35km', 'value': '35km'},
                            {'label': '40km', 'value': '40km'},
                            {'label': 'Finish', 'value': 'Finish'}
                        ],
                        value='Finish',
                        inline=True
                    ),
                    dcc.Graph(
                        id="marathon-run2-chart"
                    ),
                    html.Div(id="marathon-run2-total")

                ])
            ]
        ),
    ]
)

app.layout = html.Div([
    dcc.Location(id="url"),
    navbar,
    content
])


@app.callback(
    [Output("10k-elite-chart", "figure"),
     Output("10k-elite-total", "children")],
    [Input("10k-elite-gender-filter", "value")],
)
def update_10k_elite_chart(gender):
    print(gender)
    if gender == "M" or gender == "F":
        race_data = data["10KM ELITE"].loc[data["10KM ELITE"]
                                           ["gender"] == gender]
    else:
        race_data = data["10KM ELITE"]
    fig = px.histogram(race_data, x='chipTime hh:mm', color="gender" if gender ==
                       "C" else None, color_discrete_sequence=[FEMALE_COLOR] if gender == "F" else None, labels={'chipTime hh:mm': "Chip Time"}, title="10KM ELITE")
    # fig.update_xaxes(type='category')
    # fig.layout.xaxis.tickfont.size = 10
    fig.update_xaxes(categoryorder='array',
                     categoryarray=race_data["chipTime hh:mm"].unique())
    return fig, "Total: {}".format(race_data.shape[0])


@app.callback(
    [Output("half-marathon-elite-chart", "figure"),
     Output("half-marathon-elite-total", "children")],
    [Input("half-marathon-elite-gender-filter", "value"),
     Input("half-marathon-elite-distance-filter", "value")],
)
def update_half_marathon_elite_chart(gender, distance):
    # print(gender)
    if gender == "M" or gender == "F":
        race_data = data["HALF MARATHON ELITE"].loc[data["HALF MARATHON ELITE"]
                                                    ["gender"] == gender]
    else:
        race_data = data["HALF MARATHON ELITE"]
    hist_x = "chipTime hh:mm"
    if distance == "7km":
        hist_x = "7kmTime"
    elif distance == "9km":
        hist_x = "9kmTime"
    elif distance == "14km":
        hist_x = "14kmTime"
    elif distance == "19km":
        hist_x = "19kmTime"
    else:
        hist_x = "chipTime hh:mm"
    race_data[hist_x].replace("", float("NaN"), inplace=True)
    race_data = race_data.dropna(subset=[hist_x])
    race_data = race_data.sort_values(hist_x)
    # print(race_data[hist_x].head())
    fig = px.histogram(race_data, x=hist_x, color="gender" if gender ==
                       "C" else None, barmode="stack",
                       color_discrete_sequence=[FEMALE_COLOR] if gender == "F" else None, title="HALF MARATHON ELITE")
    fig.update_xaxes(categoryorder='array',
                     categoryarray=race_data[hist_x].unique())
    # fig.update_layout(
    #     xaxis=dict(
    #         type="category",
    #         tickmode='array',
    #         tickvals=race_data["chipTime"].tolist(),
    #         ticktext=race_data["chipTime"].tolist()
    #     )
    # )
    # fig.layout.xaxis.tickfont.size = 10
    return fig, "Total: {}".format(race_data.shape[0])


@app.callback(
    [Output("half-marathon-run1-chart", "figure"),
     Output("half-marathon-run1-total", "children")],
    [Input("half-marathon-run1-gender-filter", "value"),
     Input("half-marathon-run1-distance-filter", "value")],
)
def update_half_marathon_run1_chart(gender, distance):
    # print(gender)
    if gender == "M" or gender == "F":
        race_data = data["HALF MARATHON RUN 1"].loc[data["HALF MARATHON RUN 1"]
                                                    ["gender"] == gender]
    else:
        race_data = data["HALF MARATHON RUN 1"]
    hist_x = "chipTime hh:mm"
    if distance == "7km":
        hist_x = "7kmTime"
    elif distance == "9km":
        hist_x = "9kmTime"
    elif distance == "14km":
        hist_x = "14kmTime"
    elif distance == "19km":
        hist_x = "19kmTime"
    else:
        hist_x = "chipTime hh:mm"
    race_data[hist_x].replace("", float("NaN"), inplace=True)
    race_data = race_data.dropna(subset=[hist_x])
    race_data = race_data.sort_values(hist_x)
    # print(race_data[hist_x].head())
    fig = px.histogram(race_data, x=hist_x, color="gender" if gender ==
                       "C" else None,
                       color_discrete_sequence=[FEMALE_COLOR] if gender == "F" else None, title="HALF MARATHON RUN1")
    fig.update_xaxes(categoryorder='array',
                     categoryarray=race_data[hist_x].unique())
    # fig.layout.xaxis.tickfont.size = 10
    return fig, "Total: {}".format(race_data.shape[0])


@app.callback(
    [Output("half-marathon-run2-chart", "figure"),
     Output("half-marathon-run2-total", "children")],
    [Input("half-marathon-run2-gender-filter", "value"),
     Input("half-marathon-run2-distance-filter", "value")],
)
def update_half_marathon_run2_chart(gender, distance):
    if gender == "M" or gender == "F":
        race_data = data["HALF MARATHON RUN 2"].loc[data["HALF MARATHON RUN 2"]
                                                    ["gender"] == gender]
    else:
        race_data = data["HALF MARATHON RUN 2"]
    hist_x = "chipTime hh:mm"
    if distance == "7km":
        hist_x = "7kmTime"
    elif distance == "9km":
        hist_x = "9kmTime"
    elif distance == "14km":
        hist_x = "14kmTime"
    elif distance == "19km":
        hist_x = "19kmTime"
    else:
        hist_x = "chipTime hh:mm"
    race_data[hist_x].replace("", float("NaN"), inplace=True)
    race_data = race_data.dropna(subset=[hist_x])
    race_data = race_data.sort_values(hist_x)
    fig = px.histogram(race_data, x=hist_x, color="gender" if gender ==
                       "C" else None,
                       color_discrete_sequence=[FEMALE_COLOR] if gender == "F" else None, title="HALF MARATHON RUN1")
    fig.update_xaxes(categoryorder='array',
                     categoryarray=race_data[hist_x].unique())
    # fig.layout.xaxis.tickfont.size = 10
    return fig, "Total: {}".format(race_data.shape[0])


@app.callback(
    [Output("half-marathon-run3-chart", "figure"),
     Output("half-marathon-run3-total", "children")],
    [Input("half-marathon-run3-gender-filter", "value"),
     Input("half-marathon-run3-distance-filter", "value")],
)
def update_half_marathon_run3_chart(gender, distance):
    if gender == "M" or gender == "F":
        race_data = data["HALF MARATHON RUN 3"].loc[data["HALF MARATHON RUN 3"]
                                                    ["gender"] == gender]
    else:
        race_data = data["HALF MARATHON RUN 3"]
    hist_x = "chipTime hh:mm"
    if distance == "7km":
        hist_x = "7kmTime"
    elif distance == "9km":
        hist_x = "9kmTime"
    elif distance == "14km":
        hist_x = "14kmTime"
    elif distance == "19km":
        hist_x = "19kmTime"
    else:
        hist_x = "chipTime hh:mm"
    race_data[hist_x].replace("", float("NaN"), inplace=True)
    race_data = race_data.dropna(subset=[hist_x])
    race_data = race_data.sort_values(hist_x)
    fig = px.histogram(race_data, x=hist_x, color="gender" if gender ==
                       "C" else None,
                       color_discrete_sequence=[FEMALE_COLOR] if gender == "F" else None, title="HALF MARATHON RUN3")
    fig.update_xaxes(categoryorder='array',
                     categoryarray=race_data[hist_x].unique())
    # fig.layout.xaxis.tickfont.size = 10
    return fig, "Total: {}".format(race_data.shape[0])


@app.callback(
    [Output("marathon-elite-chart", "figure"),
     Output("marathon-elite-total", "children")],
    [Input("marathon-elite-gender-filter", "value"),
     Input("marathon-elite-distance-filter", "value")],
)
def update_marathon_elite_chart(gender, distance):
    if gender == "M" or gender == "F":
        race_data = data["MARATHON ELITE"].loc[data["MARATHON ELITE"]
                                               ["gender"] == gender]
    else:
        race_data = data["MARATHON ELITE"]
    hist_x = "chipTime hh:mm"
    if distance == "10km":
        hist_x = "10kmTime"
    elif distance == "15km":
        hist_x = "15kmTime"
    elif distance == "20km":
        hist_x = "20kmTime"
    elif distance == "Half":
        hist_x = "HalfWayTime"
    elif distance == "25km":
        hist_x = "25kmTime"
    elif distance == "30km":
        hist_x = "30kmTime"
    elif distance == "35km":
        hist_x = "35kmTime"
    elif distance == "40km":
        hist_x = "40kmTime"
    else:
        hist_x = "chipTime hh:mm"
    race_data[hist_x].replace("", float("NaN"), inplace=True)
    race_data = race_data.dropna(subset=[hist_x])
    race_data = race_data.sort_values(hist_x)
    fig = px.histogram(race_data, x=hist_x, color="gender" if gender ==
                       "C" else None,
                       color_discrete_sequence=[FEMALE_COLOR] if gender == "F" else None, title="MARATHON ELITE")
    fig.update_xaxes(categoryorder='array',
                     categoryarray=race_data[hist_x].unique())
    # fig.layout.xaxis.tickfont.size = 10
    return fig, "Total: {}".format(race_data.shape[0])


@app.callback(
    [Output("marathon-run1-chart", "figure"),
     Output("marathon-run1-total", "children")],
    [Input("marathon-run1-gender-filter", "value"),
     Input("marathon-run1-distance-filter", "value")],
)
def update_marathon_run1_chart(gender, distance):
    if gender == "M" or gender == "F":
        race_data = data["MARATHON RUN1"].loc[data["MARATHON RUN1"]
                                              ["gender"] == gender]
    else:
        race_data = data["MARATHON RUN1"]
    hist_x = "chipTime hh:mm"
    if distance == "10km":
        hist_x = "10kmTime"
    elif distance == "15km":
        hist_x = "15kmTime"
    elif distance == "20km":
        hist_x = "20kmTime"
    elif distance == "Half":
        hist_x = "HalfWayTime"
    elif distance == "25km":
        hist_x = "25kmTime"
    elif distance == "30km":
        hist_x = "30kmTime"
    elif distance == "35km":
        hist_x = "35kmTime"
    elif distance == "40km":
        hist_x = "40kmTime"
    else:
        hist_x = "chipTime hh:mm"
    race_data[hist_x].replace("", float("NaN"), inplace=True)
    race_data = race_data.dropna(subset=[hist_x])
    race_data = race_data.sort_values(hist_x)
    fig = px.histogram(race_data, x=hist_x, color="gender" if gender ==
                       "C" else None,
                       color_discrete_sequence=[FEMALE_COLOR] if gender == "F" else None, title="MARATHON ELITE")
    fig.update_xaxes(categoryorder='array',
                     categoryarray=race_data[hist_x].unique())
    # fig.layout.xaxis.tickfont.size = 10
    return fig, "Total: {}".format(race_data.shape[0])


@app.callback(
    [Output("marathon-run2-chart", "figure"),
     Output("marathon-run2-total", "children")],
    [Input("marathon-run2-gender-filter", "value"),
     Input("marathon-run2-distance-filter", "value")],
)
def update_marathon_run2_chart(gender, distance):
    if gender == "M" or gender == "F":
        race_data = data["MARATHON RUN2"].loc[data["MARATHON RUN2"]
                                              ["gender"] == gender]
    else:
        race_data = data["MARATHON RUN2"]
    hist_x = "chipTime hh:mm"
    if distance == "10km":
        hist_x = "10kmTime"
    elif distance == "15km":
        hist_x = "15kmTime"
    elif distance == "20km":
        hist_x = "20kmTime"
    elif distance == "Half":
        hist_x = "HalfWayTime"
    elif distance == "25km":
        hist_x = "25kmTime"
    elif distance == "30km":
        hist_x = "30kmTime"
    elif distance == "35km":
        hist_x = "35kmTime"
    elif distance == "40km":
        hist_x = "40kmTime"
    else:
        hist_x = "chipTime hh:mm"
    race_data[hist_x].replace("", float("NaN"), inplace=True)
    race_data = race_data.dropna(subset=[hist_x])
    race_data = race_data.sort_values(hist_x)
    fig = px.histogram(race_data, x=hist_x, color="gender" if gender ==
                       "C" else None,
                       color_discrete_sequence=[FEMALE_COLOR] if gender == "F" else None, title="MARATHON ELITE")
    fig.update_xaxes(categoryorder='array',
                     categoryarray=race_data[hist_x].unique())
    # fig.layout.xaxis.tickfont.size = 10
    return fig, "Total: {}".format(race_data.shape[0])


@app.callback(
    Output("page-content", "children"),
    [Input("url", "pathname")]
)
def render_page_content(pathname):
    if pathname == "/":
        return [layout_index]
    elif pathname == "/10k":
        return [layout_10k]
    elif pathname == "/half-marathon":
        return [layout_half_marathon]
    elif pathname == "/marathon":
        return [layout_marathon]
    # If the user tries to reach a different page, return a 404 message
    return dbc.Jumbotron(
        [
            html.H1("404: Not found", className="text-danger"),
            html.Hr(),
            html.P(f"The pathname {pathname} was not recognised..."),
        ]
    )


if __name__ == "__main__":
    app.run_server(debug=True)
server = app.server
