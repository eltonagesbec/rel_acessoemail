import os
import pandas as pd

data_arquivo_folder = 'Relatorio_Acesso'

df = []

for file in os.listdir(data_arquivo_folder):
    if file.endswith('.csv'):
        print('Carregando arquivo {0}...'.format(file))
        df.append(pd.read_csv(os.path.join(data_arquivo_folder, file)))
print(len(df))

df_principal = pd.concat(df, axis=0)
df_principal.to_csv('data/1-master_store.csv', index=False)
