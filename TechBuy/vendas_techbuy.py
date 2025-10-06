import pandas as pd
import plotly.express as px

tabela = pd.read_csv("vendas_techbuy.csv", encoding= "utf-8")
tabela = tabela.dropna()
print(tabela)
print(tabela.info())
print(tabela.describe().round(1))

tabela = tabela.drop(columns=['ID_Venda', 'Cliente_ID'])
print(tabela)

#Quais produtos mais vendem?

#Qual o faturamento mensal?

#Há diferença no comportamento dos clientes por estado?

#Existem padrões de devoluções?

#------
# Avaliando a divisão entre Pedidos Devolvidos
devolvidos = tabela["Devolvido"].value_counts()
print(devolvidos)

devolvidos_perc = tabela["Devolvido"].value_counts(normalize=True)
print(devolvidos_perc)

# Avaliando
for coluna in tabela :
    grafico = px.histogram(tabela, x=coluna, color="Devolvido")
    grafico.show()


# Produtos mais Vendidos

produtos_mais_vendidos = tabela.groupby('Produto')['Quantidade'].sum().sort_values(ascending=False).reset_index()
print(produtos_mais_vendidos)

# Gráfico dos top 5 produtos

fig = px.bar(produtos_mais_vendidos.head(5), x='Produto', y='Quantidade', title='Top 5 Produtos Mais Vendidos')
fig.show()

# Faturamento Mensal

tabela['Data_Venda'] = pd.to_datetime(tabela['Data_Venda'])
tabela['AnoMes'] = tabela['Data_Venda'].dt.to_period('M').astype(str)

faturamento_mensal = tabela.groupby('AnoMes')['Total_Venda'].sum().reset_index()
print(faturamento_mensal)

fig = px.line(faturamento_mensal, x='AnoMes', y='Total_Venda', title='Faturamento Mensal')
fig.show()

# Avaliando Clientes Por Estado
estado = tabela["Estado"].value_counts()
print(estado)

estado_perc = tabela["Estado"].value_counts(normalize=True)
print(estado_perc)

for coluna in tabela:
    graf_estado = px.histogram(tabela, x=coluna, color="Estado")
    graf_estado.show()