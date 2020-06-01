import dash
import dash_core_components as dcc
import dash_html_components as html 
from dash.dependencies import Input, Output
from django_plotly_dash import DjangoDash

import pandas as pd 
import os

from painel.views import dash

app = DjangoDash('SimpleExample', meta_tags=[{"name": "viewport", "content": "width=device-width"}])   # replaces dash.Dash

dados = pd.read_csv(os.path.join(r"painel\csv\{}".format('Teste.csv')), sep = ',', error_bad_lines = False)
dados = dados.drop(columns = ['Carimbo de data/hora','1 - Qual o seu RA?'])
x = dados.Periodo == 'Noturno'
df_noite = dados[x]

x = dados.Periodo == 'Matutino'
df_dia = dados[x]

perg = []
for item in dados:
    perg.append(item)

app.layout = html.Div([
    html.Label('Periodo'),
    dcc.Dropdown(
        id = "lista_selecao",
        options=[
            {'label': 'Noturno', 'value': 'noite'},
            {'label': u'Matutino', 'value': 'dia'},
            {'label': u'Todos', 'value': 'global'},
        ],
        value='global'
    ),
    html.Div(id="saida"),

], style={'columnCount': 2})


def dados_grafico(df): 
    dic = dict((df.groupby(by = 'Cidade onde mora').size()))
    ch = list(dic.keys())
    vl = list(dic.values())
    return ch, vl



@app.callback(
    Output('saida','children'),
    [Input('lista_selecao', 'value')]
)

def saida_update (value):
    if value == "noite":  
        x, y = dados_grafico(df_noite)
    elif value == "dia":
        x, y = dados_grafico(df_dia)
    elif value == "global":
        x, y = dados_grafico(dados)
    return dcc.Graph(
        id='plot_graph',
        figure = {
        'data': [{'x': x, 'y': y, 'type': 'bar', 'name': 'SF'}],
    }
)

