import dash_bootstrap_components as dbc
from dash import html, Input, Output
from .app import app
from .pag import page1, page2

#To display date in corner of app, uncomment this block and line in title
from datetime import date
today = date.today().strftime("%d-%b-%Y")
date_display = dbc.Col(
    html.H3(
        today,
    ),
    className="pr-3 pt-2",
)

content = dbc.Card(
            [dbc.Tabs(
                [
                dbc.Tab(label="HULL ROYAL INFIRMARY", disabled=True,
                        label_style={"font-weight": "bold", "color":"#000000"},
                        tab_style={"text-align":"left"}
                        ),
                dbc.Tab(label="Allocate",
                        tab_id="tab-1",
                        tabClassName="nav-pills",
                        #tab_style={"text-align":"center"}
                        ),
                dbc.Tab(label="Forecast",
                        tab_id="tab-2",
                        tabClassName="nav-pills",
                        ),
                dbc.Tab(label=f"{today}", disabled=True,
                        label_style={"color":"#000000"},
                        tab_style={"text-align":"right"}
                        ),
            ],
            id="tabs",
            active_tab="tab-1",
            class_name="nav-fill nav-justified",
            style={"text-align":"center",
                   "font-size": "15px",
                   },
        ),
        dbc.CardBody(id="content",
                     ),
   ],
)

title = dbc.Card(
    [
        dbc.Row(
            [
                dbc.Col(
                    html.H3("HUTH ROYAL INFIRMARY"),
                    className="pr-3 pt-2",
                ),
                dbc.Col(
                    date_display
                ),
            ],
            justify="between",
            className="p-2",
        ),
    ],
)



@app.callback(Output("content", "children"), [Input("tabs", "active_tab")])
def switch_tab(at):
    if at == "tab-1":
        return page1
    elif at == "tab-2":
        return page2
