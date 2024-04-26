# Importando a biblioteca pandas
import pandas as pd

# Carregando os dados do arquivo CSV
df = pd.read_csv('tarefa.csv', sep=';')

# Exibindo as primeiras linhas do DataFrame
print(df.head())

# Informações gerais sobre os dados
print(df.info())

# Descrição estatística dos dados
print(df.describe())

# Contagem de valores em uma coluna específica
print(df['Unnamed: 3'].value_counts())
