# Pandas Documentation: https://pandas.pydata.org/docs/getting_started/index.html#getting-started

import pandas as pd

df_main = pd.read_excel("./tabela-de-acoes.xlsx", sheet_name="main")

# print(df_main)
# print()

df_main = df_main[['Ativo', 'Data', 'Último (R$)', 'Var. Dia (%)']].copy()

# print(df_main.head(20))
# print()

df_main = df_main.rename(columns={'Ativo': 'ticker', 'Data': 'date', 'Último (R$)': 'day_last_price_brl', 'Var. Dia (%)': 'day_variation_pct'}).copy()

# print(list(df_main.columns.values))
# print()

# print(df_main.head(20))
# print()

# Creating new columns
df_main['variation_pct'] = df_main['day_variation_pct'] / 100
df_main['day_first_price_brl'] = df_main['day_last_price_brl'] / ( 1 + df_main['variation_pct'])

print(df_main)