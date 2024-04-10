# Pandas Documentation: https://pandas.pydata.org/docs/getting_started/index.html#getting-started

import pandas as pd

df_main = pd.read_excel("./tabela-de-acoes.xlsx", sheet_name="Principal")

print(df_main.head(10))