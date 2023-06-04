import dash
from dash import dcc
from dash import html
import plotly.express as px
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc
#from wordcloud import WordCloud


import pandas as pd
import pandas as pd

app = dash.Dash(__name__,external_stylesheets=[dbc.themes.BOOTSTRAP])

df = pd.read_csv('reddit_data.csv')
df['Year'] = pd.DatetimeIndex(df['date']).year
#print(df.head())

new_date = df[df.date >= '2020-01-01']
new_date = new_date[new_date.date < '2021-01-01']
new_date.sort_values('date')
new_date['Smooth_vals'] = new_date['sentiment'].rolling(int(len(df)/200)).mean()


import dash_bootstrap_components as dbc
from dash import html

#fig = px.histogram(df,x='over_18')

#
# app.layout = html.Div(
#     [
#         dbc.Row(
#             dbc.Col(
#                 html.H1("Reddit data analysis."),
#                 width={"size": 6, "offset": 3},
#             )
#         ),
#         dbc.Row(
#             [
#                 dbc.Col(
#                     html.Div([
#                     dcc.Graph(
#                     id='line-graph'
#                     ),
#                     ]),
#                     width={"size": 6, "order": 1, "offset": 1},
#                 ),
#                 dbc.Col(
#                     html.Div([
#                 dcc.Dropdown(
#                 id='my_dropdown',
#                 options=[{'label':i ,'value':i } for i in df.Year.unique()
#                          ],
#                 value=df.Year.max(),
#                 multi=False,
#                 clearable=False,
#                 className='dropDown'
#                         ),
#                         ]),
#                     width={"size": 3, "order": 2, "offset": 1},
#                 ),
#                 dbc.Col(
#                     html.Div([
#                     dcc.Graph(
#                     id='over-18',
#                     figure=fig
#                     ),
#                     ]),
#                     width={"size": 3, "order": 5,"offset":1},
#                 ),
#             ]
#         ),
#     ])

jumbotron = html.Div(
    dbc.Container(
        [
            html.H1("Reddit Sentiment Analysis", className="display-3"),
            html.P(
                "A dashboard on reddit data",
                className="lead",
            ),
            html.Hr(className="my-2"),
            html.P(
                "Use utility classes for typography and spacing to suit the "
                "larger container."
            ),
            html.P(
                dbc.Button("Learn more", color="primary"), className="lead"
            ),
        ],
        fluid=True,
        className="py-3",
    ),
    className="p-3 bg-light rounded-3",
)

app.layout = html.Div([
    html.Div([
       jumbotron
    ]),
    html.Br(),
    dbc.Container([
    dcc.Dropdown(
        id='my_dropdown',
        options=[{'label':i ,'value':i } for i in df.Year.unique()
                 ],
        value=df.Year.max(),
        multi=False,
        clearable=False,
        className='dropDown'
    ),],className='box-1'),
    html.Div([
    dcc.Graph(
        id='line-graph'
    ),],className='box-2'),
    html.Div([
    dcc.Graph(
        id='over-18',
        figure=fig
    ),],className='box-3')
], className='container')
@app.callback(
    Output(component_id='line-graph', component_property='figure'),
    [Input(component_id='my_dropdown', component_property='value')]
)
def update_graph(my_dropdown):
    date_df = df[df.Year >= my_dropdown-1]
    date_df = date_df[date_df.Year <= my_dropdown]

    fig = px.line(date_df,x='date',y='sentiment')

    return fig
if __name__ == '__main__':
    app.run_server(debug=True)