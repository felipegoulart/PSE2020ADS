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
        menu_periodo = [{'label' : itens_dropdown[i].upper(), 'value' : itens_dropdown[i].lower()}
                        for i in range(len(itens_dropdown))]

    else:
        menu_periodo = [{'label' : itens_dropdown[0].upper(), 'value' : itens_dropdown[0].lower()}]

    return menu_periodo

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