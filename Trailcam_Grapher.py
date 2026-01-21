import pandas as pd
import plotly.express as px
from dash import Dash, dcc, html, Input, Output

# Load data
df = pd.read_csv("Sample_Data_CLEANED.csv")
df['timestamp'] = pd.to_datetime(df['timestamp'])

# Extract date parts for grouping
df['year'] = df['timestamp'].dt.year
df['month'] = df['timestamp'].dt.to_period('M').dt.to_timestamp()
df['day'] = df['timestamp'].dt.to_period('D').dt.to_timestamp()

# App
app = Dash(__name__)

# Dropdown options
def dropdown_options(column):
    return [{'label': str(i), 'value': str(i)} for i in sorted(df[column].dropna().unique())]

time_options = [
    {'label': 'Day', 'value': 'day'},
    {'label': 'Month', 'value': 'month'},
    {'label': 'Year', 'value': 'year'}
]

app.layout = html.Div([
    html.H1("Trail Cam Data Viewer"),
    html.Div([
        html.Label("Group by Time:"),
        dcc.Dropdown(
            id='time-group',
            options=time_options,
            value='month',
            clearable=False
        ),
    ], style={"width": "200px", "display": "inline-block", "margin-right": "20px"}),

    html.Div([
        html.Label("Class"),
        dcc.Dropdown(id='class-filter', options=dropdown_options('class'), placeholder="Select Class")
    ], style={"width": "200px", "display": "inline-block"}),
    html.Div([
        html.Label("Order"),
        dcc.Dropdown(id='order-filter', options=dropdown_options('order'), placeholder="Select Order")
    ], style={"width": "200px", "display": "inline-block"}),
    html.Div([
        html.Label("Family"),
        dcc.Dropdown(id='family-filter', options=dropdown_options('family'), placeholder="Select Family")
    ], style={"width": "200px", "display": "inline-block"}),
    html.Div([
        html.Label("Genus"),
        dcc.Dropdown(id='genus-filter', options=dropdown_options('genus'), placeholder="Select Genus")
    ], style={"width": "200px", "display": "inline-block"}),
    html.Div([
        html.Label("Species"),
        dcc.Dropdown(id='species-filter', options=dropdown_options('species'), placeholder="Select Species")
    ], style={"width": "200px", "display": "inline-block"}),

    dcc.Graph(id='bar-graph')
])

@app.callback(
    Output('bar-graph', 'figure'),
    [Input('time-group', 'value'),
     Input('class-filter', 'value'),
     Input('order-filter', 'value'),
     Input('genus-filter', 'value'),
     Input('species-filter', 'value'),
     Input('family-filter', 'value')]
)
def update_graph(time_group, cl, order, genus, species, family):
    # Start with all data
    dff = df.copy()

    # Apply only one active filter
    for col, val in zip(['class', 'order', 'genus', 'species', 'family'], [cl, order, genus, species, family]):
        if val:
            dff = dff[dff[col] == val]
            break

    time_col = dff[time_group]
    fig = px.histogram(dff, x=time_col, nbins=len(dff[time_group].unique()), title=f"Observations Grouped by {time_group.title()}")
    fig.update_layout(xaxis_title=time_group.title(), yaxis_title="Count", bargap=0.2)
    return fig

@app.callback(
    Output('class-filter', 'value'),
    Output('order-filter', 'value'),
    Output('family-filter', 'value'),
    Output('genus-filter', 'value'),
    Output('species-filter', 'value'),
    [Input('class-filter', 'value'),
     Input('order-filter', 'value'),
     Input('family-filter', 'value'),
     Input('genus-filter', 'value'),
     Input('species-filter', 'value')]
)
def clear_others(cl, order, family, genus, species):
    inputs = [cl, order, family, genus, species]
    triggered = [i is not None for i in inputs]
    if sum(triggered) <= 1:
        return cl, order, family, genus, species
    # Reset all but the first selected
    for i, v in enumerate(triggered):
        if v:
            result = [None] * 5
            result[i] = inputs[i]
            return result

if __name__ == '__main__':
    app.run(debug=False)
