import dash
import dash_core_components as dcc
import dash_html_components as html 
from dash.dependencies import Input, Output
from django_plotly_dash import DjangoDash

import pandas as pd 
import os

from .listas import nome_graficos

app = DjangoDash('graficos')
#Importa arquivos

def Graficos(nome_arquivo):
    df = pd.read_csv(os.path.join(r"painel\csv\{}".format(nome_arquivo.nome + '.csv')), sep = ',', error_bad_lines = False)
    tabela = df.drop(columns = ['Carimbo de data/hora','1 - Qual o seu RA?', '41 - Escreva em algumas linhas sobre sua história e seus sonhos de vida.'])
    
    # Retorna os valores para a criação dos menus DROPDOWN
    def dropdown_periodo(tabela):
        lista_periodo = tabela['3 - Qual o período em que cursa?']
        itens_dropdown = list(set(lista_periodo))

        if len(itens_dropdown) > 1:
            itens_dropdown.append('Todos')
            itens_dropdown.sort(reverse=True)
            menu_periodo = [{'label' : itens_dropdown[i].upper(), 'value' : itens_dropdown[i].lower()}
                            for i in range(len(itens_dropdown))]

        else:
            menu_periodo = [{'label' : itens_dropdown[0].upper(), 'value' : itens_dropdown[0].lower()}]

        return menu_periodo

    perguntas = tabela.columns
    menu_graficos = [{'label' : str(perguntas[i]), 'value' : str(nome_graficos[i])} for i in range(len(nome_graficos))]

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

    #x, y = retorna_valores_grafico(pergunta, tabela)  parametros para chamar a função

    app.layout = html.Div(style = {'heigth' : '150px', 'position' : 'relative'}, children=[ 
        dcc.Dropdown(
            
            id = "menu_periodo",
            options= dropdown_periodo(tabela),
            value='todos'
        ),
    ],className = 'teste')

'''
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
    )'''

