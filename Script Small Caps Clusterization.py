#!pip install scipy
#!pip install scikit-learn

import pandas as pd
import yfinance as yf
from scipy.stats import zscore
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.decomposition import PCA


#%%Obter dados histórico de ações selecionadas 
#Caminho para o arquivo Excel
file_path = 'C:\\Users\\ra058832\\Desktop\\MBA\\Análise Small Caps\\Tickets.xlsx'

# Ler a planilha Excel
df = pd.read_excel(file_path)

# Assumindo que a coluna de values se chama 'Tickers'
tickers = df['Value'].tolist()

# Adicionar sufixo '.SA' para indicar que são ações listadas na B3
tickers = [ticker + '.SA' for ticker in tickers]

print(tickers)  # Verificar a lista de tickers

# Baixar dados históricos
data = yf.download(tickers, start='2019-01-01', end='2024-06-30')

# Selecionar a coluna 'Adj Close'
adj_close = data['Adj Close']

#%% Tratar dados e Criar variação semanal

# Remover colunas com valores nulos
adj_close_cleaned = adj_close.dropna(axis=1, how='any')

# Calcular os preços mensais (último preço de cada semana)
weekly_prices = adj_close_cleaned.resample('W').last()

# Calcular os retornos mensais
weekly_returns = weekly_prices.pct_change().dropna()

# Transpor o DataFrame
#weekly_returns_transposed = weekly_returns.T

#%%Construir a matriz de correlação dos retornos semanais
correlation_matrix = weekly_returns.corr()

# Visualizar a matriz de correlação
plt.figure(figsize=(12, 8))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt='.2f')
plt.title('Matriz de Correlação dos Retornos Mensais dos Ativos')
plt.show()

#%%Clusterização
# Converter a matriz de correlação em uma matriz de distância
distance_matrix = 1 - correlation_matrix

# Método do Cotovelo para determinar o número ideal de clusters
sse = []
k_range = range(1, 11)
for k in k_range:
    kmeans = KMeans(n_clusters=k, random_state=42)
    kmeans.fit(distance_matrix)
    sse.append(kmeans.inertia_)

plt.figure(figsize=(10, 6))
plt.plot(k_range, sse, marker='o')
plt.xlabel('Número de Clusters')
plt.ylabel('Soma das Distâncias ao Quadrado (Inertia)')
plt.title('Método do Cotovelo para Determinação do Número de Clusters')
plt.show()

#%% Aplicar K-means com um número de clusters
kmeans = KMeans(n_clusters=6, random_state=42)
clusters = kmeans.fit_predict(distance_matrix)

# Adicionar os clusters ao DataFrame
correlation_matrix['Cluster'] = clusters

# Visualizar os clusters usando PCA para redução de dimensionalidade
pca = PCA(n_components=2)
pca_result = pca.fit_transform(distance_matrix)

plt.figure(figsize=(10, 6))
sns.scatterplot(x=pca_result[:, 0], y=pca_result[:, 1], hue=clusters, palette='viridis')
plt.title('Clusterização de Ações - K-means')
plt.xlabel('Componente Principal 1')
plt.ylabel('Componente Principal 2')
plt.show()

# Salvar o DataFrame com os clusters
correlation_matrix.to_csv('smll_monthly_returns_clusters.csv')