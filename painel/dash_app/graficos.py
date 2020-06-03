import dash
import dash_core_components as dcc
import dash_html_components as html 
from dash.dependencies import Input, Output
from django_plotly_dash import DjangoDash

import pandas as pd 
import os

#Importa arquivos
def importa_arquivo(nome_arquivo):
    dados = pd.read_csv(os.path.join(r"painel\csv\{}".format(nome_arquivo.nome + '.csv')), sep = ',', error_bad_lines = False)
    df = df.drop(columns = ['Carimbo de data/hora','1 - Qual o seu RA?', '41 - Escreva em algumas linhas sobre sua história e seus sonhos de vida.'])
    
    return df

perguntas = df.columns

pergunta = '24 - Qual o seu conhecimento em relações aos aplicativos a seguir?   [Sistemas de Gestão Empresarial]'

#Cria a lista com dicionários de perguntas e respostas
def cria_questoes(df):
    dic = []
    dff = {}
    for items in df:
        dic = (dict(df.groupby(by= items).size()))
        dff[items] = dic
    
    return dff

def retorna_valores_grafico(pergunta, df):
    questoes = cria_questoes(df)

    chave = []
    valor = []

    chave.extend(list(questoes[pergunta].keys()))
    valor.extend(list(questoes[pergunta].values()))

    return chave, valor

x, y = retorna_valores_grafico(pergunta, df)


    app.layout = html.Div(style={'columnCount': 1}, children = [
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

    ])


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
