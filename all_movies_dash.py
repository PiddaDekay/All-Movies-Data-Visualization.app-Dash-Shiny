## More Layout, with a familiar graph

import dash
from dash.dependencies import Input
from dash.dependencies import Output
import dash_core_components as dcc
import dash_html_components as html
from numpy.core.fromnumeric import sort
import pandas as pd
import numpy as np
import plotly.express as px

app = dash.Dash(__name__)
data = pd.read_csv('all_movies.csv')
df=data[['Rated','Year','Genre','Rating10','Rotten','BoxOffice']]
df = df.dropna()
genre_set = df['Genre'].unique()
genre= []
for i in range(len(genre_set)):
    for j in range(len(genre_set[i].split(', '))):
        genre.append(genre_set[i].split(', ')[j])

genre = pd.Series(genre).unique()
rating = df['Rated'].unique()


app.layout = html.Div([
	html.H1('Movie Revenue Analysis'),
    html.H3('Select Genre'),
    dcc.Dropdown(
        id='genre',
        options=[
            {'label':'All', 'value': 'All'},
            {'label':'Drama', 'value':'Drama'}, 
            {'label':'History', 'value':'History'}, 
            {'label':'Sci-Fi', 'value':'Sci-Fi'}, 
            {'label':'Crime', 'value':'Crime'}, 
            {'label':'Thriller', 'value':'Thriller'}, 
            {'label':'War', 'value':'War'},
            {'label':'Film-Noir', 'value':'Film-Noir'}, 
            {'label':'Adventure', 'value':'Adventure'}, 
            {'label':'Family', 'value':'Family'}, 
            {'label':'Fantasy', 'value':'Fantasy'}, 
            {'label':'Comedy', 'value':'Comedy'}, 
            {'label':'Romance', 'value':'Romance'},
            {'label':'Mystery', 'value':'Mystery'}, 
            {'label':'Western', 'value':'Western'}, 
            {'label':'Action', 'value':'Action'}, 
            {'label':'Musical', 'value':'Musical'}, 
            {'label':'Horror', 'value':'Horror'}, 
            {'label':'Biography', 'value':'Biography'},
            {'label':'Music', 'value':'Music'}, 
            {'label':'Documentary', 'value':'Documentary'}, 
            {'label':'Animation', 'value':'Animation'}, 
            {'label':'Sport', 'value':'Sport'}, 
            {'label':'Short', 'value':'Short'}, 
            {'label':'News', 'value':'News'}
        ],
        value = 'All'

    ),
    html.Div(id='output_genre'),
    html.H3('Select Range of Year'),
    dcc.RangeSlider(
        id='range_of_year',
        min=min(df['Year']),
        max=max(df['Year']),
        step=1,
        marks={
            1925:'1925',
            1940:'1940',
            1960:'1960',
            1980:'1980',
            2000:'2000',
            2014:'2014',
        },
        value=[min(df['Year']),max(df['Year'])]
    ),
    html.Div(id='output_roy'),
    html.H3('Select Rating'),
    dcc.Dropdown(
        id='rating',
        options=[
            {'label':'All', 'value': 'All'},
            {'label':'Unrated', 'value':'Unrated'}, 
            {'label':'Not Rated', 'value':'Not Rated'}, 
            {'label':'Approved', 'value':'Approved'}, 
            {'label':'PG', 'value':'PG'}, 
            {'label':'PG-13', 'value':'PG-13'}, 
            {'label':'R', 'value':'R'},
            {'label':'G', 'value':'G'}, 
            {'label':'NC-17', 'value':'NC-17'}, 
            {'label':'TV-PG', 'value':'TV-PG'}, 
            {'label':'Atp', 'value':'Atp'}, 
            {'label':'MA15+', 'value':'MA15+'}
        ],
        value = 'All'

    ),
    html.Div(id='output_rating'),
    dcc.Graph(id = 'scatter1',style={'width': '80vh', 'height': '80vh','display': 'inline-block'}),
    dcc.Graph(id = 'scatter2',style={'width': '80vh', 'height': '80vh','display': 'inline-block'})
])

@app.callback(
    dash.dependencies.Output('output_genre', 'children'),
    [dash.dependencies.Input('genre', 'value')])
def update_output(value):
    return 'You have selected "{}"'.format(value)

@app.callback(
    dash.dependencies.Output('output_roy', 'children'),
    [dash.dependencies.Input('range_of_year', 'value')])
def update_output(value):
    return 'You have selected "{}"'.format(value)

@app.callback(
    dash.dependencies.Output('output_rating', 'children'),
    [dash.dependencies.Input('rating', 'value')])
def update_output(value):
    return 'You have selected "{}"'.format(value)


@app.callback(
     dash.dependencies.Output('scatter1','figure'),
    [dash.dependencies.Input('rating', 'value'),
     dash.dependencies.Input('range_of_year','value'),
     dash.dependencies.Input('genre','value')]
)
def update_graph(rating,range_of_year,genre):
    if(genre=='All'):
        if(rating=='All'):
            select_rows = (df['Year']>=range_of_year[0]) & (df['Year']<=range_of_year[1])
            x1 = df[select_rows]
        else:
            select_rows = (df['Year']>=range_of_year[0]) & (df['Year']<=range_of_year[1]) & (df['Rated']==rating)
            x1 = df[select_rows]
    else:
        if(rating=='All'):
            select_rows = (df['Year']>=range_of_year[0]) & (df['Year']<=range_of_year[1]) & (df['Genre'].str.contains(genre))
            x1 = df[select_rows]
        else:
            select_rows = (df['Year']>=range_of_year[0]) & (df['Year']<=range_of_year[1]) & (df['Genre'].str.contains(genre)) & (df['Rated']==rating)
            x1 = df[select_rows]
        #dataframe
       # xnew1 = x1
    fig = px.scatter(x1, x='Rating10',y='BoxOffice')
    fig.update_traces(mode='markers',marker_size=10)
    fig.update_xaxes()
    fig.update_yaxes()
    fig.update_layout()
    return fig

@app.callback(
     dash.dependencies.Output('scatter2','figure'),
    [dash.dependencies.Input('rating', 'value'),
     dash.dependencies.Input('range_of_year','value'),
     dash.dependencies.Input('genre','value')]
)
def update_graph(rating,range_of_year,genre):
    if(genre=='All'):
        if(rating=='All'):
            select_rows = (df['Year']>=range_of_year[0]) & (df['Year']<=range_of_year[1])
            x1 = df[select_rows]
        else:
            select_rows = (df['Year']>=range_of_year[0]) & (df['Year']<=range_of_year[1]) & (df['Rated']==rating)
            x1 = df[select_rows]
    else:
        if(rating=='All'):
            select_rows = (df['Year']>=range_of_year[0]) & (df['Year']<=range_of_year[1]) & (df['Genre'].str.contains(genre))
            x1 = df[select_rows]
        else:
            select_rows = (df['Year']>=range_of_year[0]) & (df['Year']<=range_of_year[1]) & (df['Genre'].str.contains(genre)) & (df['Rated']==rating)
            x1 = df[select_rows]
        #dataframe
       # xnew1 = x1
    fig = px.scatter(x1, x='Rotten',y='BoxOffice')
    fig.update_traces(mode='markers',marker_size=10)
    fig.update_xaxes()
    fig.update_yaxes()
    fig.update_layout()
    return fig

if __name__ == '__main__':
    app.run_server(debug=True)