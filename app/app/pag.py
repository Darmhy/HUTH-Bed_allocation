import dash_bootstrap_components as dbc

from .components import (
    forecast_block,
    patient_details_block,
    suggested_moves_block,
    virtual_hospital_block,
)

page1 = dbc.Card(
        [
            dbc.Row(
                    [
                        dbc.Col(
                        virtual_hospital_block,
                        width=12,
                        xl=12,
                        className="p-0",
                        style={"border": "none"}
                ),
                    ],
                className="m-0",
            ),
            dbc.Row(
                [
                    dbc.Col(
                        patient_details_block,
                        width=12,
                        xl=6,
                        className="p-0",
                    ),
                    dbc.Col(
                        suggested_moves_block,
                        width=12,
                        xl=6,
                        className="p-0"
                    ),
                ],
                className="m-0",
            ),
        ], style={"border": "none"}
)

page2 = dbc.Card(
            [
                dbc.Row(
                    [
                    dbc.Col(
                        forecast_block,width=12, xl=12,
                        className="p-0"
                    ),
                   ],
                className="p-2",
                justify="end",
                style={"border": "none"}
                ),
        ], className="p-0", style={"border": "none"}
)