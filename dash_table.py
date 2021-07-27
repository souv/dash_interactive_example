# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.

import dash
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Input, Output
import plotly.express as px 
import pandas as pd

df = pd.read_csv('https://gist.githubusercontent.com/chriddyp/c78bf172206ce24f77d6363a2d754b59/raw/c353e8ef842413cae56ae3920b8fd78468aa4cb2/usa-agricultural-exports-2011.csv')

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

# def generate_table(dataframe, max_rows=10):
#     return html.Table([
#         html.Thead(
#             html.Tr([html.Th(col) for col in dataframe.columns])
#         ),
#         html.Tbody([
#             html.Tr([
#                 html.Td(dataframe.iloc[i][col]) for col in dataframe.columns
#             ]) for i in range(min(len(dataframe), max_rows))
#         ])
#     ])

app.layout = html.Div([
    html.Div([
                dcc.Dropdown(
                    id='yaxis-column',
                    options=[{'label': i, 'value': i} for i in df.columns],
                    value='pork'
                ),
            ],
            style={'width': '48%', 'display': 'inline-block'}),

    dcc.Graph(id='indicator-graphic')

])

@app.callback(
    Output('indicator-graphic', 'figure'),
    Input('yaxis-column', 'value')
)

def update_graph(yaxis_column_name):
    dff = df

    fig = px.scatter(x=dff['beef'],
                     y=dff[yaxis_column_name])

    fig.update_layout(margin={'l': 40, 'b': 40, 't': 10, 'r': 0}, hovermode='closest')

    fig.update_yaxes(title=yaxis_column_name)

    return fig


if __name__ == '__main__':
    app.run_server(debug=True)