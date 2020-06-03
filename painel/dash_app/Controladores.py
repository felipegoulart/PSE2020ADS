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

print(x, y)