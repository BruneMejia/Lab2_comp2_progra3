import pandas as pd
import csv
import numpy as np

#Cargar el dataset 
datos = pd.read_csv("datos_libros.csv")
#print(datos)

#Resumen estadistico del dataset
print("resumen estadistico del dataset:")
print(datos.describe())

#Tipos de datos por columna
print("Tipos de datos por columna:")
print(datos.dtypes)

#Primeros cinco registros
print("Primeros cinco registros")
print(datos.head())

#Ultimos cinco registros
print("Ultimos cinco registros")
print(datos.tail())

# Libros ordenados por edad de interes
print("Libros ordenados por edad de interes:")
print(datos.sort_values(by="Inerest_age", ascending=False))

#Media
print(f"Media: {(datos['Inerest_age'].dropna())}")
#Mediana
print(f"Mediana: {(datos['Inerest_age'].dropna())}")


