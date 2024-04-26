# Importando a biblioteca pandas
import pandas as pd

# Carregando os dados do arquivo CSV
df = pd.read_csv('tarefa.csv', sep=';')

# Encontrando a linha da tarefa que você deseja alterar
tarefas = df[df['Unnamed: 3'] == 'Nome da Tarefa']

if not tarefas.empty:
    indice_tarefa = tarefas.index[0]
else:
    print("Não há nenhuma tarefa com o nome 'Nome da Tarefa'")
