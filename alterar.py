# Importando a biblioteca pandas
import pandas as pd

# Carregando os dados do arquivo CSV
df = pd.read_csv('tarefa.csv', sep=';')

# Alterando uma linha específica
df.loc[0] = ['Novo Valor1', 'Novo Valor2', 'Novo Valor3', 'Novo Valor4', 'Novo Valor5', 'Novo Valor6', 'Novo Valor7', 'Novo Valor8', 'Novo Valor9', 'Novo Valor10', 'Novo Valor11', 'Novo Valor12', 'Novo Valor13', 'Novo Valor14', 'Novo Valor15', 'Novo Valor16']

# Exibindo as primeiras linhas do DataFrame para verificar as mudanças
print(df.head())
