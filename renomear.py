# Importando a biblioteca pandas
import pandas as pd

# Carregando os dados do arquivo CSV
df = pd.read_csv('tarefa.csv', sep=';')

# Renomeando as colunas
df.columns = ['Coluna1', 'Coluna2', 'Coluna3', 'Coluna4', 'Coluna5', 'Coluna6', 'Coluna7', 'Coluna8', 'Coluna9', 'Coluna10', 'Coluna11', 'Coluna12', 'Coluna13', 'Coluna14', 'Coluna15', 'Coluna16']

# Exibindo as primeiras linhas do DataFrame para verificar as mudanças
print(df.head())
