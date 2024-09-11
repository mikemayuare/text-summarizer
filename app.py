import os
import gunicorn
from dash import Dash, html, Input, Output, State, callback
import dash_bootstrap_components as dbc
from textSummarizer.pipeline.prediciton import PredictionPipeline


app = Dash(external_stylesheets=[dbc.themes.MATERIA])

# app.layout = dbc.Alert("Hello, Bootstrap!", className="m-5")

app.layout = html.Div(
    [
        html.Div(
            [
                dbc.NavbarSimple(
                    children=[
                        dbc.NavItem(dbc.NavLink("Page 1", href="#")),
                        dbc.DropdownMenu(
                            children=[
                                dbc.DropdownMenuItem("More pages", header=True),
                                dbc.DropdownMenuItem("Page 2", href="#"),
                                dbc.DropdownMenuItem("Page 3", href="#"),
                            ],
                            nav=True,
                            in_navbar=True,
                            label="More",
                        ),
                    ],
                    brand="Text Summarizer",
                    brand_href="#",
                    color="primary",
                    dark=True,
                )
            ]
        ),
        html.Div(
            [
                dbc.Row(
                    [
                        dbc.Col(
                            [
                                html.H2("Input"),
                                dbc.Textarea(
                                    id="text-input",
                                    placeholder="Enter text",
                                    style={"width": "100%", "height": 300},
                                ),
                                dbc.Button(
                                    "Summarize",
                                    id="button-submit",
                                    className="pa-1 mt-2 ms-auto",
                                    n_clicks=0,
                                ),
                            ],
                            width=4,
                        ),
                        dbc.Col(
                            [
                                html.H2("Summary"),
                                html.Div(
                                    id="text-output", style={"whiteSpace": "pre-line"}
                                ),
                            ],
                            width=4,
                        ),
                    ],
                    className="mt-5",
                    justify="center",
                )
            ]
        ),
    ]
)


@callback(
    Output("text-output", "children"),
    Input("button-submit", "n_clicks"),
    State("text-input", "value"),
)
def predict(n_clicks, text):
    if n_clicks == 0:
        return None
    else:
        try:
            pipe = PredictionPipeline()
            summary = pipe.predict(text)
            return summary
        except Exception as e:
            raise e


if __name__ == "__main__":
    app.run(debug=True)
