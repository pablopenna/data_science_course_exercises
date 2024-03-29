# -*- coding: utf-8 -*-
"""pampero_pandas.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1bI8hCJIULZiI1Pa-DgFbuWh-v9uq5agZ
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = pd.read_csv('./titanic.csv')

# 1
print(data.shape)
print(data.head(10))

#2 
print(data[data['PassengerId']==148])

#3
print(data[data.index%2==0])

#4
print(data[data.Pclass==1].sort_values("Name",ascending=True).Name)

#5
print(data.groupby("Survived").size() / data.shape[0] * 100)
print(data.Survived.value_counts() / len(data) * 100)

#6
# Total percentage
print(data.groupby(["Pclass","Survived"]).size() / len(data)*100)
# Percentage per class
print(data.groupby(["Pclass","Survived"]).size() / data.groupby(["Pclass"]).size())

#Official result
data.groupby("Pclass")["Survived"].mean()
data.groupby("Pclass")["Survived"].value_counts(normalize=True)

#7
# Passengers with missing Age
data[data.Age.isna()][["Age", "Name"]]

index2Drop = data[data.Age.isna()].index
data.drop(index2Drop)

#official result
data.dropna(subset=["Age"])
#alternative | '~' negates
data[~data.Age.isna()]

#8
data[data.Sex=="female"].groupby(["Pclass"]).Age.mean()

#9
data["Young"] = data["Age"] < 18
data.head(5)

#10
data.groupby(["Pclass", "Young"])["Survived"].value_counts(normalize=True)

data.groupby(["Pclass", "Young"])["Survived"].mean()

"""---------------------------------------------------------

"""

d2016 = pd.read_csv('./emisiones-2016.csv', sep=";")
d2017 = pd.read_csv('./emisiones-2017.csv', sep=";")
d2018 = pd.read_csv('./emisiones-2018.csv', sep=";")
d2019 = pd.read_csv('./emisiones-2019.csv', sep=";")

# 1
data = pd.concat([d2016,d2017,d2018,d2019],axis=0).reset_index(drop=True)
data

# 2
columnas = ["ESTACION","MUNICIPIO"]
columnas = columnas + [col for col in data.columns if col[0]=='D']
subdata = data[columnas]

# 3
subdata50 = subdata[subdata.index<subdata.shape[0]/2]
print(subdata.shape)
print(subdata50.shape)

# 4
dataMerged = pd.merge(subdata50, d2018, how='inner')
dataMerged.shape