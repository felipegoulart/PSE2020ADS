import dash
import dash_core_components as dcc
import dash_html_components as html 
from dash.dependencies import Input, Output
from django_plotly_dash import DjangoDash

import pandas as pd 
import os

#importa as funções para maior organização do código
from .auxiliar import nome_graficos, dropdown_periodo, cria_questoes, retorna_valores_grafico, faixa_etaria

app = DjangoDash('graficos')
#Importa arquivos

def Graficos(nome_arquivo):
    df = pd.read_csv(os.path.join(r"painel\csv\{}".format(nome_arquivo.nome + '.csv')), sep = ',', error_bad_lines = False)
    tabela = df.drop(columns = ['Carimbo de data/hora','1 - Qual o seu RA?', '41 - Escreva em algumas linhas sobre sua história e seus sonhos de vida.'])
    tabela = tabela.drop(57)
    
    perg = []
    for item in tabela:
        perg.append(item)

    perguntas = tabela.columns

    menu_graficos = [{'label' : str(nome_graficos[i]), 'value' : str(perg[i]) } for i in range(len(nome_graficos))]

    pergunta = '24 - Qual o seu conhecimento em relações aos aplicativos a seguir?   [Sistemas de Gestão Empresarial]'

    #x, y = retorna_valores_grafico(pergunta, tabela)  parametros para chamar a função

    app.layout = html.Div(
            [
                html.Div(
                [
                    dcc.Dropdown(
                        id = "menu_periodo",
                        options= dropdown_periodo(tabela),
                        value='Todos'
                    ),
                    dcc.Dropdown(
                        id = "menu_graficos",
                        options= menu_graficos,
                        value= perg[1]
                    ),        
                ],
                className = 'teste',
                style = {'columnCount': 2}
                ),

                html.Div(
                    [
                        dcc.Graph(id = 'grafico')
                    ]
                )
            ]
        )

    @app.callback(
        Output('grafico','figure'),
        [Input('menu_periodo', 'value'),
        Input('menu_graficos', 'value')]
    )   
    def retorna_grafico (menu_periodo, menu_graficos):
        i = perg.index(menu_graficos)
        per = perg[i]
        x, y = retorna_valores_grafico(menu_graficos, tabela, menu_periodo)
        data = [
            dict(
                type = 'pie',
                name = 'gr',
                labels = x,
                values = y,
                direction = 'clockwise'     
            )
        ]
        figura = dict(data = data)
        return figura
        