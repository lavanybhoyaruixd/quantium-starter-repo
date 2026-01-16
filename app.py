import pandas as pd
from dash import Dash, dcc, html, Input, Output
import plotly.express as px

# Load data
df = pd.read_csv("processed_sales.csv")
df.columns = df.columns.str.strip()
df["Date"] = pd.to_datetime(df["Date"])
df = df.sort_values("Date")

# Initialize Dash app
app = Dash(__name__)

app.layout = html.Div(
    className="container",
    children=[
        html.H1(
            "Soul Foods – Pink Morsel Sales Visualiser",
            className="header"
        ),

        html.Div(
            className="controls",
            children=[
                html.Label("Select Region:"),

                dcc.RadioItems(
                    id="region-filter",
                    options=[
                        {"label": "All", "value": "all"},
                        {"label": "North", "value": "north"},
                        {"label": "East", "value": "east"},
                        {"label": "South", "value": "south"},
                        {"label": "West", "value": "west"},
                    ],
                    value="all",
                    inline=True
                )
            ]
        ),

        html.Div(
            className="graph-container",
            children=[
                dcc.Graph(id="sales-graph")
            ]
        )
    ]
)

@app.callback(
    Output("sales-graph", "figure"),
    Input("region-filter", "value")
)
def update_graph(selected_region):
    if selected_region == "all":
        filtered_df = df
    else:
        filtered_df = df[df["Region"].str.lower() == selected_region]

    fig = px.line(
        filtered_df,
        x="Date",
        y="Sales",
        color="Region",
        labels={"Sales": "Total Sales", "Date": "Date"},
        title="Pink Morsel Sales Over Time"
    )

    fig.add_vline(
        x=pd.to_datetime("2021-01-15"),
        line_dash="dash",
        line_color="red"
    )

    return fig


if __name__ == "__main__":
    app.run_server(debug=True)
