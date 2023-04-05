import dash_bootstrap_components as dbc
from dash import Input, Output, html
from .app import app
from .pag import page1, page2


tabs = html.Div(
    [
        dbc.Col(
                    html.H3("HULL ROYAL INFIRMARY"),
                    className="pr-3 pt-2",
                ),
        dbc.Tabs(
            [
                dbc.Tab(label="Allocate", tab_id="tab-1"),
                dbc.Tab(label="Forecast", tab_id="tab-2"),
            ],
            id="tabs",
            active_tab="tab-1",
        ),
        html.Div(id="content"),
    ]
)


@app.callback(Output("content", "children"), [Input("tabs", "active_tab")])
def switch_tab(at):
    if at == "tab-1":
        return page1
    elif at == "tab-2":
        return page2