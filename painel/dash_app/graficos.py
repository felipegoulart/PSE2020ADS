import dash
import dash_core_components as dcc
import dash_html_components as html 
from dash.dependencies import Input, Output
from django_plotly_dash import DjangoDash

import pandas as pd 
import os

#importa as funções para maior organização do código
from .auxiliar import nome_graficos

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

    def dropdown_periodo(tabela):
        lista_periodo = tabela['3 - Qual o período em que cursa?']
        itens_dropdown = list(set(lista_periodo))
        if len(itens_dropdown) > 1:
            itens_dropdown.append('Todos')
            itens_dropdown.sort(reverse=True)
            menu_periodo = [{'label' : itens_dropdown[i].upper(), 'value' : itens_dropdown[i]}
                            for i in range(len(itens_dropdown))]

        else:
            menu_periodo = {'label' : itens_dropdown[0].upper(), 'value' : itens_dropdown[0]}

        return menu_periodo

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
            ], style={
                    "height": "60px",
                    "width": "auto",
                    "margin-bottom": "25px",
                },
        )

    def filtro(periodo_selecionado, pergunta_selecionada, tabela):
        periodo = []
        if periodo_selecionado == 'Todos':
            periodo.extend(periodo_selecionado)
            pergunta = pergunta_selecionada
            lista_resposta = list(tabela[pergunta])
            coluna = pd.DataFrame(lista_resposta, columns = [pergunta])

        else:
            periodo.append(periodo_selecionado)
            pergunta = pergunta_selecionada
            dff = tabela[tabela['3 - Qual o período em que cursa?'].isin(periodo)] 
            lista_resposta = list(dff[pergunta])
            coluna = pd.DataFrame(lista_resposta, columns = [pergunta])

        return coluna

    def separar(tabela, pergunta):
        coluna = list(tabela[pergunta])
        respostas = []
        for i in range(len(coluna)):
            respostas.extend(coluna[i].split(';'))
        df_respostas = pd.DataFrame(respostas, columns= [pergunta])
        respostas_agrupadas = dict(df_respostas.groupby(by = pergunta).size())
        return respostas_agrupadas

    def faixa_etaria(tabela, pergunta):    
        anos = list(tabela[pergunta])
        data_atual = datetime.now()

        respostas = {
            'Dados inválidos' : 0,
            '17 á 20 anos' : 0,
            '21 á 30 anos' : 0,
            '31 á 40 anos' : 0,
            '41 anos ou mais' : 0
        }

        for ano in anos:
            data_nascimento = datetime.strptime(ano, '%Y-%m-%d')
            dias = (data_atual - data_nascimento).days
            idade = int(dias / 364)

            if idade < 17:
                respostas['Dados inválidos'] += 1
            elif idade >= 17 and idade <= 20:
                respostas['17 á 20 anos'] += 1
            elif idade >= 21 and idade <= 30:
                respostas['21 á 30 anos'] += 1
            elif idade >= 31 and idade <= 40:
                respostas['31 á 40 anos'] += 1
            else:
                respostas['41 anos ou mais'] += 1 

        return respostas

    def cria_questoes(tabela, pergunta):
        coluna = tabela
        respostas = dict(coluna.groupby(by= pergunta).size())

        return respostas


    def retorna_valores_grafico(data):

        chave = []
        valor = []
        
        chave.extend(list(data.keys()))
        valor.extend(list(data.values()))

        return chave, valor

    def selecao_grafico (data, numero_perg):
        x, y = retorna_valores_grafico(data)
        if numero_perg in [2,3,4,6,9,13,17,18,19,21,22,25,26,27,31,32,36,38,39]:
            grafico = dict(
                    type = 'pie',
                    name = 'gr',
                    labels = x,
                    values = y
                    )
        else:
            grafico = dict(
                    type = 'bar',
                    name = 'gr',
                    x = x,
                    y = y
                    )
        return grafico


    @app.callback(
        Output('grafico','figure'),
        [Input('menu_periodo', 'value'),
        Input('menu_graficos', 'value')]
    )   
    def retorna_grafico (menu_periodo, menu_graficos):
        dados_filtrados = filtro(menu_periodo,menu_graficos, tabela)
        nome_coluna = list(dados_filtrados)
        numero_perg = int(nome_coluna[0][:2])

        if numero_perg in [28,33]:
            data = separar(dados_filtrados, menu_graficos)
        elif numero_perg == 7:
            data = faixa_etaria(dados_filtrados, menu_graficos)
        else:
            data = cria_questoes(dados_filtrados, menu_graficos)
        
        grafico = selecao_grafico(data, numero_perg)
        dados_grafico = [grafico]
        figure = dict(data = dados_grafico)

        return figure
        