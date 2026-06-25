import pandas as pd
from dash import Dash, html, dcc, Input, Output
import plotly.express as px

# Read data
df = pd.read_csv("formatted_output.csv")
df["date"] = pd.to_datetime(df["date"])

app = Dash(__name__)

app.layout = html.Div([
    html.H1("Soul Foods Pink Morsel Sales Visualiser"),

    dcc.RadioItems(
        id="region-filter",
        options=[
            {"label": "All", "value": "all"},
            {"label": "North", "value": "north"},
            {"label": "South", "value": "south"},
            {"label": "East", "value": "east"},
            {"label": "West", "value": "west"},
        ],
        value="all",
        inline=True
    ),

    dcc.Graph(id="sales-chart")
])

@app.callback(
    Output("sales-chart", "figure"),
    Input("region-filter", "value")
)
def update_chart(region):

    if region == "all":
        filtered = df
    else:
        filtered = df[df["region"] == region]

    chart_data = filtered.groupby("date", as_index=False)["sales"].sum()

    fig = px.line(
        chart_data,
        x="date",
        y="sales",
        title="Pink Morsel Sales"
    )

    fig.update_layout(
        xaxis_title="Date",
        yaxis_title="Sales"
    )

    return fig

if __name__ == "__main__":
    app.run(debug=True)