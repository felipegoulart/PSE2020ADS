import dash
import dash_core_components as dcc
import dash_html_components as html 
from dash.dependencies import Input, Output
from django_plotly_dash import DjangoDash

import pandas as pd 
import os

#importa as funções para maior organização do código
from .auxiliar import nome_graficos, dropdown_periodo, cria_questoes, retorna_valores_grafico

app = DjangoDash('graficos')
#Importa arquivos

def Graficos(nome_arquivo):
    df = pd.read_csv(os.path.join(r"painel\csv\{}".format(nome_arquivo.nome + '.csv')), sep = ',', error_bad_lines = False)
    tabela = df.drop(columns = ['Carimbo de data/hora','1 - Qual o seu RA?', '41 - Escreva em algumas linhas sobre sua história e seus sonhos de vida.'])
    tabela = df.drop(57)

    perguntas = tabela.columns

    menu_graficos = [{'label' : str(nome_graficos[i]), 'value' : int(i)} for i in range(len(nome_graficos))]

    pergunta = '24 - Qual o seu conhecimento em relações aos aplicativos a seguir?   [Sistemas de Gestão Empresarial]'



    #x, y = retorna_valores_grafico(pergunta, tabela)  parametros para chamar a função

    app.layout = html.Div(
            [
                html.Div(
                [
                    dcc.Dropdown(
                        id = "menu_periodo",
                        options= dropdown_periodo(tabela),
                        value='todos'
                    ),
                    dcc.Dropdown(
                        id = "menu_graficos",
                        options= menu_graficos,
                        value= perguntas[1]
                    ),        
                ],
                className = 'teste',
                style = {'columnCount': 2}
                ),
                html.Div(
                    [
                        dcc.Graph(id = 'grafico')
                ])
            ])

    '''def dados_grafico(df): 
        dic = dict((df.groupby(by = 'Cidade onde mora').size()))
        ch = list(dic.keys())
        vl = list(dic.values())
        return ch, vl

    @app.callback(
        Output('grafico','figure'),
        [Input('menu_periodo', 'value'),
        Input('menu_graficos', 'value')]
    )   
    def retorna_grafico (menu_periodo, menu_graficos):
        i = int(menu_graficos)
        pergunta = perg[i]
        x, y = retorna_valores_grafico(pergunta, tabela)
        return html.Div(
                    [dcc.Graph(
                        id = 'grafico',
                        figure = {
                            'data': [{ 'x': x, 'y': y, 'type': 'bar'}]
                            }
                    )]
                )
    perg = []
    for item in tabela:
        perg.append(item)'''
