# Pandas Documentation: https://pandas.pydata.org/docs/getting_started/index.html#getting-started

import pandas as pd

# Changes all float cells to a given format
pd.options.display.float_format = '{:.2f}'.format


# Gettting the Main spreadsheet
df_main = pd.read_excel("./tabela_de_acoes.xlsx", sheet_name="main")


# Getting specific columns
df_main = df_main[['Ativo', 'Data', 'Último (R$)', 'Var. Dia (%)']].copy()


# Renaming columns
df_main = df_main.rename(columns={'Ativo': 'ticker', 'Data': 'date', 'Último (R$)': 'day_last_price_brl', 'Var. Dia (%)': 'day_variation_pct'}).copy()


# Creating new columns
df_main['variation_pct'] = df_main['day_variation_pct'] / 100
df_main['day_first_price_brl'] = df_main['day_last_price_brl'] / ( 1 + df_main['variation_pct'])

print()
print(df_main.head(10))


# Getting the all_stocks sheet and merging it into df_main
df_all_stocks = pd.read_excel("./tabela_de_acoes.xlsx", sheet_name="all_stocks")
df_all_stocks = df_all_stocks.rename(columns={'Código': 'ticker', 'Qtde. Teórica': 'total_stocks'})

df_main = df_main.merge(df_all_stocks, left_on='ticker', right_on='ticker', how='left')

df_main['total_stocks'] = df_main['total_stocks'].astype(int)

print()
print(df_main.head(10))


df_main['total_variation_brl'] = (df_main['day_last_price_brl'] - df_main['day_first_price_brl']) * df_main['total_stocks']

print()
print(df_main.head(10))


# Creating a new column and apply the validation for each cell (x) in 'total_variation_brl'
df_main['result'] = df_main['total_variation_brl'].apply(lambda x: '+' if x > 0 else ('-' if x < 0 else '='))

print()
print(df_main)


# Getting stock names from a different sheet
df_name = pd.read_excel("./tabela_de_acoes.xlsx", sheet_name="name")
df_name = df_name.rename(columns={'Ticker': 'ticker', 'Nome': 'name'})

df_main = df_main.merge(df_name, left_on='ticker', right_on='ticker', how='left')
	
print()
print(df_main)