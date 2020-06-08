from datetime import datetime
import pandas as pd

#Lista com os novos nomes das tabelas
nome_graficos = [
    'Cursos',
    'Periodo',
    'Estado em que nasceu',
    'Cidade de residência',
    'Genêro',
    'Faixa Etária',
    'Estado Civil',
    'Portador de necessidade especial',
    'Quantidade de filhos',
    'Com quem o estudante mora',
    'Quantidade de pessoas morando no domicílio',
    'Situação do domicílio',
    'A quanto tempo mora no domicílio',
    'Faixa de renda mensal da família',
    'Quantidade de intens no domicílio (Televisores)',
    'Quantidade de intens no domicílio (Video cassete e/ou DVD)',
    'Quantidade de intens no domicílio (Rádios)',
    'Quantidade de intens no domicílio (Automóveis)',
    'Quantidade de intens no domicílio (Motocicleta)',
    'Quantidade de intens no domicílio (Celular Comum)',
    'Quantidade de intens no domicílio (Smartphone)',
    'Quantidade de intens no domicílio (Microcomputador de mesa)',
    'Quantidade de intens no domicílio (Notebook)',
    'Possuí no domicílio (Telefone)',
    'Possuí no domicílio (Internet)',
    'Possuí no domicílio (Tv por assinatura )',
    'Possuí no domicílio (Empregada Mensalista)',
    'Possuí Trabalho',
    'Vinculo empregáticio',
    'Área de atuação',
    'Horário de trabalho',
    'Possuí plano de saúde',
    'Escolaridade da mãe',
    'Escolaridade do pai',
    'Aonde estudou',
    'Qual a frequência que utiliza microcomputadores',
    'Onde utiliza o microcomputador (Em casa)',
    'Onde utiliza o microcomputador (No trabalho)',
    'Onde utiliza o microcomputador (Na escola)',
    'Onde utiliza o microcomputador (Em outros lugares)',
    'Uso de microcomputador para trabalhos profissionais',
    'Uso de microcomputador para trabalhos escolares',
    'Uso de microcomputador para entretenimento',
    'Uso de microcomputador para comunicação por e-mail',
    'Uso de microcomputador para operações bancárias',
    'Uso de microcomputador para Compras eletrônicas',
    'Conhecimento em informática',
    'Conhecimento em Windows',
    'Conhecimento em Linux',
    'Conhecimento em Editores de texto',
    'Conhecimento em Planilhas eletrônicas',
    'Conhecimento em Apresentadores(Powerpoint, Impress, Prezzi etc.)',
    'Conhecimento em Sistemas de Gestão Empresárial',
    'Conhecimento em Inglês',
    'Conhecimento em Espanhol',
    'Conhecimento em outros idiomas',
    'Meio por onde busca informações (TV)',
    'Meio por onde busca informações (Internet)',
    'Meio por onde busca informações (Revista)',
    'Meio por onde busca informações (Rádio)',
    'Meio por onde busca informações (Redes Sociais)',
    'Meio por onde busca informações (Conversa com amigos)',
    'Frequência em que se lê jornais',
    'Assunstos que mais se lê em jornais',
    'Livros lido por ano em média(Não considerando os escolares)',
    'Genêro literário preferido',
    'Dedica parte do tempo para atividades voluntárias',
    'Religião',
    'Fontes de entreterimento cultural',
    'Como conheceu a FATEC',
    'Porque escolheu o curso',
    'Maiores expectativas quanto ao curso',
    'Expectativas após se formar',
    'Já estudaram nesta instituição',
    'Fez algum curso técnico',
    'Meio de transporte utilizado para ir a faculdade'
]

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

#Cria a lista com dicionários de perguntas e respostas
def cria_questoes(tabela,periodo,pergunta):
    coluna = filtro(periodo , pergunta, tabela)
    coluna = dict(coluna.groupby(by= pergunta).size())

    return coluna

def retorna_valores_grafico(pergunta, df, periodo):
    
    questoes = cria_questoes(df, periodo, pergunta)
    perg = []
    for item in df:
        perg.append(item)
    elemento = perg.index(pergunta)
    chave = []
    valor = []
    
    chave.extend(list(questoes.keys()))
    valor.extend(list(questoes.values()))

    return chave, valor

def selecao_grafico (pergunta,df,periodo):
    x, y = retorna_valores_grafico(pergunta,df,periodo)
    if int(pergunta[:2]) in [2,3,4,6,9,13,17,18,19,21,22,25,26,27,31,32,36,38,39]:
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

def retorna_df (df, periodo):
    if periodo == 'Todos':
        df = df
    else:
        x = df['3 - Qual o período em que cursa?'] == periodo.title()
        df = df[x]
    return df

def faixa_etaria(tabela, pergunta):
    pergunta_respostas = {}    
    anos = list(tabela[pergunta])
    data_atual = datetime.now()
    dicio_faixa_etaria = {
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
            dicio_faixa_etaria['Dados inválidos'] += 1
        elif idade >= 17 and idade <= 20:
            dicio_faixa_etaria['17 á 20 anos'] += 1
        elif idade >= 21 and idade <= 30:
            dicio_faixa_etaria['21 á 30 anos'] += 1
        elif idade >= 31 and idade <= 40:
            dicio_faixa_etaria['31 á 40 anos'] += 1
        else:
            dicio_faixa_etaria['41 anos ou mais'] += 1
        
    pergunta_respostas[pergunta] = dicio_faixa_etaria

    
    return pergunta_respostas

def separar(tabela, pergunta):
    coluna = list(tabela[pergunta])
    respostas = []
    for i in range(len(coluna)):
        respostas.extend(coluna[i].split(';'))
    df_respostas = pd.DataFrame(respostas, columns= [pergunta])
    respostas_agrupadas = df_respostas.groupby(by = pergunta).size()
    return respostas_agrupadas


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