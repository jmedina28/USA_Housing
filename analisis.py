import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv("USA_Housing.csv")
print(df)

print("Las columnas del dataset son :\n", df.columns)
print("La descripción del dataset es la siguiente: \n", df.describe())

# calcula la media , mediana, desviación estándar, varianza y el valor máximo y mínimo


def analisis(dataset, var):
    print(f"La media de la columna {var} es: ", dataset[var].mean())
    print(f"La mediana de la columna {var} es: ", dataset[var].median())
    print(
        f"La desviación estándar de la columna {var} es: ", dataset[var].std())
    print(f"La varianza de la columna {var} es: ", dataset[var].var())
    print(f"El valor máximo de la columna {var} es: ", dataset[var].max())
    print(f"El valor mínimo de la columna {var} es: ", dataset[var].min())
    print("\n")


# extraemos una lista que contiene las columnas que vamos a analizar
lista = []
for i in df.columns:
    if df[i].dtype == np.int64 or df[i].dtype == np.float64:
        lista.append(i)
# llamamos a analisis para cada columna
for i in lista:
    analisis(df, i)
# relacion entre precio e ingresos
plt.figure(figsize=(10, 10))
plt.scatter(df['Price'], df['Avg. Area Income'])
plt.xlabel('Precio de la vivienda')
plt.ylabel('Ingreso medio del propietario')
plt.show()
# relacion entre precio y el numero de habitantes
plt.figure(figsize=(10, 10))
plt.scatter(df['Price'], df['Avg. Area Number of Rooms'])
plt.xlabel('Precio de la vivienda')
plt.ylabel('Número de habitaciones')
plt.show()
# relaciona precio y antiguedad
plt.figure(figsize=(10, 10))
plt.scatter(df['Price'], df['Avg. Area House Age'])
plt.xlabel('Precio de la vivienda')
plt.ylabel('Edad')
plt.show()
# este print devuelve la antiguedad de la casa con mayor precio
print("="*100)
print("La antigüedad de la casa con mayor precio es: ",
      df['Avg. Area House Age'][df['Price'].idxmax()], "\n")
# obtengo df2 que contiene casas con antiguedad inferior a 6 años
df2 = df[df['Avg. Area House Age'] < 6]
# halla el precio medio de las casas con antiguedad menor que 6
lista2 = []
for i in df2.columns:
    if df2[i].dtype == np.int64 or df2[i].dtype == np.float64:
        lista2.append(i)
# llamamos a analisis para cada columna
print("="*100)
print("Aquí está el analisis de las casas con antiguedad menor que 6 años: \n")
for i in lista2:
    analisis(df2, i)