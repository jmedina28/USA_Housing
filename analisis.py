import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv("USA_Housing.csv")
print(df)

print("Las columnas del dataset son :\n", df.columns)
print("La descripción del dataset es la siguiente: \n", df.describe())

# calcula la media , mediana, desviación estándar y el valor máximo y mínimo
def analisis(var):    
    print(f"La media de la columna {var} es: ", df[var].mean())
    print(f"La mediana de la columna {var} es: ", df[var].median())
    print(f"La desviación estándar de la columna {var} es: ", df[var].std())
    print(f"El valor máximo de la columna {var} es: ", df[var].max())
    print(f"El valor mínimo de la columna {var} es: ", df[var].min())
    print("\n")
# extraemos una lista que contiene las columnas que vamos a analizar
lista = []
for i in df.columns:
    if df[i].dtype == np.int64 or df[i].dtype == np.float64:
        lista.append(i)
# llamamos a analisis para cada columna
for i in lista:
    analisis(i)
# relacion entre precio e ingresos
plt.figure(figsize=(10,10))
plt.scatter(df['Price'], df['Avg. Area Income'])
plt.xlabel('Precio de la vivienda')
plt.ylabel('Ingreso medio del propietario')
plt.show()
# relacion entre precio y el numero de habitantes
plt.figure(figsize=(10,10))
plt.scatter(df['Price'], df['Avg. Area Number of Rooms'])
plt.xlabel('Precio de la vivienda')
plt.ylabel('Número de habitaciones')
plt.show()