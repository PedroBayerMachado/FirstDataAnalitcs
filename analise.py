import pandas as pd
import plotly.express as px

tabela = pd.read_csv("top50.csv", encoding="latin1")
tabela = tabela.rename(columns={"Beats.Per.Minute" : "BPM","Loudness..dB.." : "Volume", "Valence." : "Positivity"})
tabela = tabela[["BPM", "Volume", "Energy", "Danceability", "Positivity"]]

tabela["BPM"] = tabela["BPM"] / 2
tabela["Volume"] = (tabela["Volume"] + 11) * 10
print(tabela.describe())

tabela_media = tabela.mean()
print(tabela_media)

grafico = px.line_polar(r=tabela_media.values, theta=tabela_media.index, range_r=[0,100], line_close=True, title="Analise De Dados Top 50 Spotify", template="plotly_dark")

grafico.show()