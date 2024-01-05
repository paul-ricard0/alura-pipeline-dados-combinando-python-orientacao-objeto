import json
import csv

from processamento_dados import Dados


path_json = 'data_raw/dados_empresaA.json'
path_csv = 'data_raw/dados_empresaB.csv'


print('\n>>>>>>>>> Extract <<<<<<<<<<<<')
dados_empresaA = Dados.leitura_dados(path_json, 'json')
print(f'Nome colunas EmpresaA: {dados_empresaA.nome_colunas}')
print(f'QTD de linhas EmpresaA: {len(dados_empresaA.dados)}')

dados_empresaB = Dados.leitura_dados(path_csv, 'csv')
print(f'Nome colunas EmpresaB: {dados_empresaB.nome_colunas}')
print(f'QTD de linhas EmpresaB: {len(dados_empresaB.dados)}')


print('\n\n>>>>>>>>> Transform <<<<<<<<<<<<')
key_mapping = {'Nome do Item': 'Nome do Produto',
                'Classificação do Produto': 'Categoria do Produto',
                'Valor em Reais (R$)': 'Preço do Produto (R$)',
                'Quantidade em Estoque': 'Quantidade em Estoque',
                'Nome da Loja': 'Filial',
                'Data da Venda': 'Data da Venda'}

dados_empresaB.rename_columns(key_mapping=key_mapping)
print(f'Nome colunas EmpresaB: {dados_empresaB.nome_colunas}')


dados_fusao = Dados.join(dados_empresaA, dados_empresaB)
print(f'Nome colunas fusão: {dados_fusao.nome_colunas}')
print(f'QTD de linhas fusão: {len(dados_fusao.dados)}')


print('\n\n>>>>>>>>> Load <<<<<<<<<<<<')
path_dados_combinados = 'data_processed/dados_combinados_class.csv'
dados_fusao.salvando_dados (path_dados_combinados)
print(path_dados_combinados)