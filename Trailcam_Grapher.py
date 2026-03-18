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

# Create consistent color mapping for all species
color_palette = [
    "#1f77b4", "#ff7f0e", "#2ca02c", "#d62728", "#9467bd",
    "#8c564b", "#e377c2", "#7f7f7f", "#17becf", "#aec7e8",
    "#ffbb78", "#98df8a", "#ff9896", "#c5b0d5", "#c49c94"
]
all_common_names = sorted(df['common_name'].dropna().unique())
species_colors = {name: color_palette[i % len(color_palette)] for i, name in enumerate(all_common_names)}

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
                html.Label("Plot Type:"),
                dcc.Dropdown(
                    id='plot-type',
                    options=[
                        {'label': 'Histogram', 'value': 'histogram'},
                        {'label': 'Stacked Bar Plot', 'value': 'stacked_bar'}
                    ],
                    value='histogram',
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
     Input('plot-type', 'value'),
     Input('class-filter', 'value'),
     Input('order-filter', 'value'),
     Input('genus-filter', 'value'),
     Input('species-filter', 'value'),
     Input('family-filter', 'value')]
)
def update_graph(time_group, plot_type, cl, order, genus, species, family):
    # Start with all data
    dff = df.copy()

    # Apply only one active filter
    for col, val in zip(['class', 'order', 'genus', 'species', 'family'], [cl, order, genus, species, family]):
        if val:
            dff = dff[dff[col] == val]
            break

    time_col = dff[time_group]
    if plot_type == 'histogram':
        fig = px.histogram(dff, x=time_col, nbins=len(dff[time_group].unique()), title=f"🌍 Observations Grouped by {time_group.title()}")
    else:  # stacked_bar
        grouped = dff.groupby([time_group, 'common_name']).size().reset_index(name='count')
        # Calculate total per time group
        totals = grouped.groupby(time_group)['count'].sum().reset_index(name='total')
        grouped = grouped.merge(totals, on=time_group)
        grouped['percentage'] = (grouped['count'] / grouped['total']) * 100
        # Sort by common_name to ensure consistent order
        grouped = grouped.sort_values('common_name')
        # Use consistent color mapping
        fig = px.bar(grouped, x=time_group, y='percentage', color='common_name', barmode='stack', title=f"🌍 Stacked Observations by {time_group.title()}",
                     color_discrete_map=species_colors, category_orders={'common_name': sorted(grouped['common_name'].unique())})
    
    # Apply nature theme to graph
    fig.update_layout(
        xaxis_title=time_group.title(),
        yaxis_title="Percentage (%)" if plot_type == 'stacked_bar' else "Count",
        bargap=0.2,
        title_font_size=18,
        title_font_color="#2d5a3d",
        font=dict(family="Arial, sans-serif", size=12, color="#2d3d2d"),
        plot_bgcolor="#f5f5f0",
        paper_bgcolor="white",
        hovermode="x unified",
        margin=dict(l=50, r=50, t=80, b=50),
    )
    
    if plot_type == 'histogram':
        fig.update_traces(
            marker_color="#4a7c59",
            marker_line_color="#2d5a3d",
            marker_line_width=1.5,
            hovertemplate="<b>%{x}</b><br>Count: %{y}<extra></extra>"
        )
    else:
        # Explicitly set colors for each species trace
        for trace in fig.data:
            species_name = trace.name
            if species_name in species_colors:
                trace.marker.color = species_colors[species_name]
        fig.update_traces(
            hovertemplate="<b>%{x}</b><br>%{fullData.name}: %{y:.1f}% (Count: %{customdata})<extra></extra>",
            customdata=grouped['count'].values
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
