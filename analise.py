import pandas as pd
import matplotlib.pyplot as plt

# Leitura dos dados
dados = [1649,1458,1694,1956,1429,1973,1730,1359,1662,1361,1360,1572,925,982,1331,1196,1594,1227,1077,1939,1432,1520,1072,1336,1154,1612,1319,1412,1380,1510]

df = pd.DataFrame(dados, columns=['vendas'])
print("Média:", df['vendas'].mean())
print("Mediana:", df['vendas'].median())
print("Desvio Padrão:", df['vendas'].std())
print("Máximo:", df['vendas'].max())
print("Mínimo:", df['vendas'].min())

plt.hist(df['vendas'], bins=10)
plt.title("Distribuição de Vendas")
plt.savefig("grafico.png")
print("Análise completa!")
