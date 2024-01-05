import json
import csv

def leitura_json(path_json):
    dados_json = []
    with open(path_json, 'r') as file:
        dados_json = json.load(file)
    return dados_json

def leitura_csv(path_csv):
    dados_csv = []
    with open(path_csv, 'r') as file:
        spamreader = csv.DictReader(file, delimiter=',')
        for row in spamreader:
            dados_csv.append(row)
    return dados_csv

def leitura_dados(path, tipo_arquivo):
    dados = []
    if tipo_arquivo == 'csv':
        dados = leitura_csv(path)
    elif tipo_arquivo == 'json':
        dados = leitura_json(path)
    return dados

def get_columns(dados):
    return list(dados[0].keys())

def rename_columns(dados, key_mapping):
    new_dados_csv = []

    for old_dict in dados:
        dict_temp = {}
        for old_key, value in old_dict.items():
            dict_temp[key_mapping[old_key]] = value
        new_dados_csv.append(dict_temp)
        
    return new_dados_csv

def join(dadosA, dadosB):
    combined_list = []
    combined_list.extend(dadosA)
    combined_list.extend(dadosB)
    return combined_list

def transformando_dados_tabela(dados, nomes_colunas):
    dados_combinados_tabela = [nomes_colunas]
    for row in dados:
        linha = []
        for coluna in nomes_colunas:
            linha.append(row.get(coluna, 'Indisponivel'))
        dados_combinados_tabela.append(linha)
    
    return dados_combinados_tabela

def salvando_dados(dados, path):
    with open(path, 'w') as file:
        writer = csv.writer(file)
        writer.writerows(dados)

path_json = 'data_raw/dados_empresaA.json'
path_csv = 'data_raw/dados_empresaB.csv'

print('\n>>>> Iniciando a Leitura <<<<')
dados_json = leitura_dados(path_json, 'json')
print(f'Colunas json: {get_columns(dados_json)}')
print(f"Tamanho dos dados json: {len(dados_json)}")
print(f'Dados json:\n{dados_json[0]}')

dados_csv = leitura_dados(path_csv, 'csv')
print(f'\nColunas csv: {get_columns(dados_csv)}')
print(f"Tamanho dos dados csv: {len(dados_csv)}")
print(f'Dados csv:\n{dados_csv[0]}')

print('\n>>>> Transformando os dados <<<<')
key_mapping = {'Nome do Item': 'Nome do Produto',
                'Classificação do Produto': 'Categoria do Produto',
                'Valor em Reais (R$)': 'Preço do Produto (R$)',
                'Quantidade em Estoque': 'Quantidade em Estoque',
                'Nome da Loja': 'Filial',
                'Data da Venda': 'Data da Venda'}

dados_csv = rename_columns(dados_csv, key_mapping)
print(f'Novas colunas CSV: {get_columns(dados_csv)}')

print('\n>>>> Fusão dos dados <<<<')
dados_fusao = join(dados_json, dados_csv)
print(f'Colunas fusao: {get_columns(dados_fusao)}')
print(f"Tamanho dos dados fusao: {len(dados_fusao)}")

print('\n>>>> Salvando os dados <<<<')
dados_fusao_tabela = transformando_dados_tabela(dados_fusao, get_columns(dados_fusao))

path_dados_combinados = 'data_processed/dados_combinados.csv'
salvando_dados(dados_fusao_tabela, path_dados_combinados)
print(path_dados_combinados)