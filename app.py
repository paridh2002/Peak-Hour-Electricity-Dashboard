import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import plotly.express as px

from processor import load_and_process, train_model

# Load data
df = load_and_process()
model = train_model(df)

app = dash.Dash(__name__)

app.layout = html.Div([
    html.H1("Peak Hour Electricity Usage Dashboard"),

    dcc.Dropdown(
        id="dorm-select",
        options=[{"label": dorm, "value": dorm} for dorm in df["dorm"].unique()],
        value="Dorm_A"
    ),

    dcc.Graph(id="usage-graph")
])

@app.callback(
    Output("usage-graph", "figure"),
    Input("dorm-select", "value")
)
def update_graph(selected_dorm):
    filtered_df = df[df["dorm"] == selected_dorm]

    fig = px.line(
        filtered_df,
        x="timestamp",
        y="usage",
        title=f"Electricity Usage for {selected_dorm}"
    )

    return fig

if __name__ == "__main__":
    app.run(debug=True)

