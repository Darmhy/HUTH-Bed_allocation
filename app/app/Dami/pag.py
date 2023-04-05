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
                        virtual_hospital_block, width=12, xl=12, className="p-0"
                    ),
                ],
                className="mt-3",
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
                        suggested_moves_block, width=12, xl=6, className="p-0"
                    ),
                ],
                className="m-0",
            ),
        ]
)

page2 = dbc.Card(
            [
                dbc.Row(
                    [
                    dbc.Col(
                        forecast_block,
                            ),
                    ],
                className="p-2", justify="end",),
        ], className="p-0",
)