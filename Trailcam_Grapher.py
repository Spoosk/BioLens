import os
import pandas as pd
import plotly.express as px
from dash import Dash, dcc, html, Input, Output

# Load data (expects CSV cleaned by CSVDateCleaner which may add a 'camera' column)
DATA_FILE = "Sample_Data_CLEANED.csv"
CAMERA_COORDS_FILE = "camera_coords.csv"  # optional: columns camera,lat,lon

if not os.path.exists(DATA_FILE):
    raise FileNotFoundError(f"Data file not found: {DATA_FILE}")

df = pd.read_csv(DATA_FILE)
if 'timestamp' in df.columns:
    df['timestamp'] = pd.to_datetime(df['timestamp'], errors='coerce')
else:
    df['timestamp'] = pd.NaT

# Extract date parts for grouping
if not df['timestamp'].isna().all():
    df['year'] = df['timestamp'].dt.year
    df['month'] = df['timestamp'].dt.to_period('M').dt.to_timestamp()
    df['day'] = df['timestamp'].dt.to_period('D').dt.to_timestamp()
else:
    df['year'] = None
    df['month'] = None
    df['day'] = None

# Optional camera coordinates
camera_coords = None
if os.path.exists(CAMERA_COORDS_FILE):
    try:
        camera_coords = pd.read_csv(CAMERA_COORDS_FILE)
    except Exception:
        camera_coords = None

app = Dash(__name__)

# Helper to build dropdown options from dataframe columns
def dropdown_options(column):
    if column not in df.columns:
        return []
    return [{'label': str(i), 'value': str(i)} for i in sorted(df[column].dropna().unique())]

time_options = [
    {'label': 'Day', 'value': 'day'},
    {'label': 'Month', 'value': 'month'},
    {'label': 'Year', 'value': 'year'}
]

mode_options = [
    {'label': 'Chart', 'value': 'chart'},
    {'label': 'Heatmap', 'value': 'heatmap'}
]

app.layout = html.Div([
    html.H1("Trail Cam Data Viewer"),

    html.Div([
        html.Label("Group by Time:"),
        dcc.Dropdown(id='time-group', options=time_options, value='month', clearable=False),
    ], style={"width": "200px", "display": "inline-block", "margin-right": "20px"}),

    html.Div([html.Label("Mode:"), dcc.RadioItems(id='mode', options=mode_options, value='chart')], style={"display": "inline-block", "margin-right": "20px"}),

    html.Div([html.Label("Camera"), dcc.Dropdown(id='camera-filter', options=dropdown_options('camera'), placeholder="Select Camera")], style={"width": "200px", "display": "inline-block"}),

    html.Div([html.Label("Class"), dcc.Dropdown(id='class-filter', options=dropdown_options('class'), placeholder="Select Class")], style={"width": "200px", "display": "inline-block"}),
    html.Div([html.Label("Order"), dcc.Dropdown(id='order-filter', options=dropdown_options('order'), placeholder="Select Order")], style={"width": "200px", "display": "inline-block"}),
    html.Div([html.Label("Family"), dcc.Dropdown(id='family-filter', options=dropdown_options('family'), placeholder="Select Family")], style={"width": "200px", "display": "inline-block"}),
    html.Div([html.Label("Genus"), dcc.Dropdown(id='genus-filter', options=dropdown_options('genus'), placeholder="Select Genus")], style={"width": "200px", "display": "inline-block"}),
    html.Div([html.Label("Species"), dcc.Dropdown(id='species-filter', options=dropdown_options('species'), placeholder="Select Species")], style={"width": "200px", "display": "inline-block"}),

    dcc.Graph(id='bar-graph')
])


@app.callback(
    Output('bar-graph', 'figure'),
    [Input('time-group', 'value'),
     Input('mode', 'value'),
     Input('camera-filter', 'value'),
     Input('class-filter', 'value'),
     Input('order-filter', 'value'),
     Input('genus-filter', 'value'),
     Input('species-filter', 'value'),
     Input('family-filter', 'value')]
)
def update_graph(time_group, mode, camera, cl, order, genus, species, family):
    dff = df.copy()

    # Apply camera filter (exact match)
    if camera and 'camera' in dff.columns:
        dff = dff[dff['camera'] == camera]

    # Apply only one taxonomic filter (preserve existing behavior)
    for col, val in zip(['class', 'order', 'genus', 'species', 'family'], [cl, order, genus, species, family]):
        if val:
            dff = dff[dff[col] == val]
            break

    # Heatmap mode: require camera_coords with lat/lon
    if mode == 'heatmap':
        if camera_coords is None or not {'camera', 'lat', 'lon'}.issubset(camera_coords.columns):
            # Return empty figure with instruction
            fig = px.scatter(title='Heatmap requires camera_coords.csv with columns: camera,lat,lon')
            return fig

        # Count detections per camera
        counts = dff.groupby('camera').size().reset_index(name='count')
        merged = camera_coords.merge(counts, on='camera', how='left').fillna(0)
        # Use scatter_mapbox sized by count; density_mapbox can be used if many points
        fig = px.scatter_mapbox(merged, lat='lat', lon='lon', size='count', hover_name='camera', color='count', size_max=40,
                                title='Detections Heatmap (by camera)', zoom=12, mapbox_style='open-street-map')
        return fig

    # Default chart mode: time histogram
    if time_group not in dff.columns:
        fig = px.histogram(title='No valid time grouping available')
        return fig

    time_col = dff[time_group]
    fig = px.histogram(dff, x=time_col, nbins=len(dff[time_group].dropna().unique()), title=f"Observations Grouped by {time_group.title()}")
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
