import pandas as pd
import plotly.express as px

# Lendo o ClientesBanco.csv

tabela = pd.read_csv("ClientesBanco.csv", encoding="latin1")
tabela = tabela.drop("CLIENTNUM", axis=1)

print(tabela)
# Tratando valores vazios e exibindo resumo das colunas
tabela = tabela.dropna()
print(tabela.info())

print(tabela.describe().round(1))

# Avaliando a divisão entre Clientes e Cancelados
qtde_categotia = tabela["Categoria"].value_counts()
print(qtde_categotia)

qtde_categoria_perc = tabela["Categoria"].value_counts(normalize=True)
print(qtde_categoria_perc)

# Temos vários formas de descobrir o motivo de cancelamento

# Podemos olhar a comparação entre Clientes e Cancelados
# em cada uma das colunas da nossa base de dados
# para ver se essa informação traz algum insight novo para a gente

for coluna in tabela :
    grafico = px.histogram(tabela, x=coluna, color="Categoria")
    grafico.show()

