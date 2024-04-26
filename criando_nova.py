# Importando a biblioteca pandas
import pandas as pd

# Carregando os dados do arquivo CSV
df = pd.read_csv('tarefa.csv', sep=';')

# Encontrando a linha da tarefa que você deseja alterar
indice_tarefa = df[df['Unnamed: 3'] == 'Nome da Tarefa'].index[0]

# Alterando a tarefa
df.loc[indice_tarefa, 'Unnamed: 3'] = 'Nova Tarefa'

# Exibindo as primeiras linhas do DataFrame para verificar as mudanças
print(df.head())
