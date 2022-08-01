import pandas as pd
from sklearn.tree import DecisionTreeClassifier
import joblib

dataset = pd.read_csv('deportes.csv')
inputs = dataset.drop(columns=['deporte'])
outputs = dataset['deporte']

modelo = DecisionTreeClassifier()
modelo.fit(inputs, outputs)
predicciones = modelo.predict([ [1,24], [2,33] ])
