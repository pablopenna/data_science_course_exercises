from os import rename
import pandas as pd 
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import seaborn as sns
import sklearn
from sklearn import preprocessing
from sklearn.cluster import KMeans

df_ventas = pd.read_csv('./OnlineRetail.csv', sep=',', encoding="ISO-8859-1")

###
#  DATA COMPREHENSION
###

# has nulls
print(df_ventas.isna().sum())

# check data integrity
print(df_ventas.describe())

# ignore NaN customerIds
df_ventas = df_ventas.dropna(subset=["CustomerID"]).reset_index(drop=True)

# remove rows with negative quantity (Returns)
df_ventas = df_ventas[df_ventas['Quantity']>0].reset_index(drop=True)

# adjust format
df_ventas['CustomerID'] = df_ventas['CustomerID'].astype(np.int32).astype(np.str)

# Select only data we are interested in
df_ventas = df_ventas[['CustomerID','InvoiceDate','Quantity','UnitPrice']]

###
#   Data preparation
###

# Get total price per entry (Quantity * UnitPrice)
df_ventas['venta'] = df_ventas['Quantity'] * df_ventas['UnitPrice']

# Transform dates to only day
df_ventas['InvoiceDate'] = pd.to_datetime(df_ventas['InvoiceDate'], format='%d-%m-%Y %H:%M').dt.date

# Group per client + day
df_ventas_agg = df_ventas.groupby(['CustomerID','InvoiceDate'])['venta'].sum().reset_index()

# Change column names
df_ventas_agg.columns = ['CustomerID','dt_venta','venta']

print(df_ventas_agg.head())

###
#   Visualizations
###

# No of clients
print(f"We have {df_ventas_agg['CustomerID'].unique().shape[0]} clients")

# Days of purchase
# ...
df_tmp_dias_compra = df_ventas_agg.groupby('CustomerID').size().reset_index().rename({0: 'dias de compra'}, axis=1)
print(df_tmp_dias_compra)

# Dates where there are most purchases
df_tmp_fechas = df_ventas_agg.groupby('dt_venta').size().reset_index().rename({0: 'clientes'}, axis=1)
print(df_tmp_fechas)


###
#   VARIABLE CONSTRUCTION
###

# frequency - average days between purchases

# calculate previous date of purchase
df_ventas_agg['dt_venta_lag'] = df_ventas_agg.groupby('CustomerID')['dt_venta'].shift(1)
df_ventas_agg['dt_venta_diff'] = df_ventas_agg['dt_venta'] - df_ventas_agg['dt_venta_lag']
df_ventas_agg['dt_venta_diff'] = df_ventas_agg['dt_venta_diff'].apply(lambda x : x.days if str(x)!='NaT' else 365).astype(np.int32)


df_ventas_agg['constante'] = 1
df_clientes = df_ventas_agg.groupby('CustomerID').agg({
    'venta': np.sum,
    'dt_venta_diff': np.mean,
    'constante': np.sum
}).reset_index()
#.rename({
#    0: 'CustomerID',
#    1: 'suma_ventas',
#}, axis=1).reset_index()

print(df_clientes)


###
# REDUCIR VALORES ATIPICOS / REDUCE REMOVE OUTLIERS
###

# https://medium.com/@dilekamadushan/introduction-to-k-means-clustering-7c0ebc997e00https://towardsdatascience.com/k-means-a-complete-introduction-1702af9cd8c?gi=fbd55c57e841

# Values of 'venta' is very disperse and has some rare high values
# df_clientes.describe()

df_clientes['venta'] = np.clip(df_clientes['venta'], 0, np.quantile(df_clientes['venta'], 0.95))


## Normalize data
col_variables = ['venta', 'dt_venta_diff', 'constante']
scaler = preprocessing.StandardScaler()
#scaler = preprocessing.MinMaxScaler()
#scaler = preprocessing.QuantileTransformer()
scaler.fit(df_clientes[col_variables])
df_clientes_norm = scaler.transform(df_clientes[col_variables])
df_clientes_norm = pd.DataFrame(df_clientes_norm) #Get is as dataframe since scaler.transform returns a numpu array
df_clientes_norm.columns = col_variables

## Modelado - Classify clients in clusters.
model = KMeans(n_clusters=3, max_iter=10)
model.fit(df_clientes_norm)
df_clientes_norm['cluster'] = model.labels_

## Tecnica del codo para encontrar numero de segmentos optimos (a usar durante el modelado)
# En la gráfica resultante mirar donde estaría el codo si el grafo fuese un brazo.

distances = []
range_n_clusters = [2,3,4,5,6,7,8,9,10]
for n_cluster in range_n_clusters:
    kmeans = KMeans(n_clusters=n_cluster, max_iter=10)
    kmeans.fit(df_clientes_norm)
    distances.append(kmeans.inertia_)

fig, ax = plt.subplots()
ax.plot(distances)
plt.figure(figsize=(12,6))
plt.show()


###
# PROFILING
###
#plt.figure(figsize=(12,6))
#sns.boxplot(x='cluster', y='venta', data=df_clientes)
#plt.show()

# sns.boxplot(x="variable",y="value",data=pd.melt(df_data[['Income', 'gastos_totales]]))
# sns.boxplot(x="Income",y="gastos_totales",data=df_data)