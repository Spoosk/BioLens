import pandas as pd
import plotly.express as px
from dash import Dash, dcc, html, Input, Output
import sys

# Load data from command line argument if provided
csv_file = "Sample_Data_CLEANED.csv"
if len(sys.argv) > 1:
    csv_file = sys.argv[1]

df = pd.read_csv(csv_file)
df['timestamp'] = pd.to_datetime(df['timestamp'])

# Extract date parts for grouping
df['year'] = df['timestamp'].dt.year
df['month'] = df['timestamp'].dt.to_period('M').dt.to_timestamp()
df['day'] = df['timestamp'].dt.to_period('D').dt.to_timestamp()

# App
app = Dash(__name__)

# Note: CSS is loaded automatically from assets/custom.css

# Dropdown options
def dropdown_options(column):
    return [{'label': str(i), 'value': str(i)} for i in sorted(df[column].dropna().unique())]

time_options = [
    {'label': 'Day', 'value': 'day'},
    {'label': 'Month', 'value': 'month'},
    {'label': 'Year', 'value': 'year'}
]

app.layout = html.Div([
    html.Div([
        html.H1("🌿 Trail Cam Data Viewer"),
        html.Div([
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
        ], style={"margin-bottom": "30px", "padding": "20px", "background-color": "white", "border-radius": "8px", "box-shadow": "0 2px 8px rgba(0,0,0,0.1)"}),
    ], style={"padding": "20px", "max-width": "1400px", "margin": "0 auto"}),
    
    html.Div([
        dcc.Graph(id='bar-graph', style={"height": "600px"})
    ], style={"padding": "20px", "max-width": "1400px", "margin": "0 auto"})
], style={"background-color": "#f5f5f0", "min-height": "100vh", "padding": "20px"})


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
    fig = px.histogram(dff, x=time_col, nbins=len(dff[time_group].unique()), title=f"🌍 Observations Grouped by {time_group.title()}")
    
    # Apply nature theme to graph
    fig.update_layout(
        xaxis_title=time_group.title(),
        yaxis_title="Count",
        bargap=0.2,
        title_font_size=18,
        title_font_color="#2d5a3d",
        font=dict(family="Arial, sans-serif", size=12, color="#2d3d2d"),
        plot_bgcolor="#f5f5f0",
        paper_bgcolor="white",
        hovermode="x unified",
        margin=dict(l=50, r=50, t=80, b=50),
    )
    
    fig.update_traces(
        marker_color="#4a7c59",
        marker_line_color="#2d5a3d",
        marker_line_width=1.5,
        hovertemplate="<b>%{x}</b><br>Count: %{y}<extra></extra>"
    )
    
    fig.update_xaxes(
        showgrid=True,
        gridwidth=1,
        gridcolor="#e8e8e0",
        zeroline=False,
        showline=True,
        linewidth=2,
        linecolor="#4a7c59"
    )
    
    fig.update_yaxes(
        showgrid=True,
        gridwidth=1,
        gridcolor="#e8e8e0",
        zeroline=False,
        showline=True,
        linewidth=2,
        linecolor="#4a7c59"
    )
    
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
