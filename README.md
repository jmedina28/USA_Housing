<h1 align="center">USA Housing</h1>

---
En este [repositorio](https://github.com/jmedina28/USA_Housing) queda resuelto el ejercicio de USA Housing. Para llevar a cabo el proyecto me he documentado a través de la teoría que se encuentra en el campus virtual y otras fuentes.
***
## Enunciado
Realice un EDA sobre el dataset propuesto intentando encontrar realaciones entre las variables (características) que proporciona. Utilice las herramientas empleadas durante el análisis del dataset del Titanic. 

Reutilice todo el código posible ya visto adaptándolo a este nuevo dataset o busque otras formas de obtener resultados con otras librerías o herramientas de programación de Python. *** Nota: Esta tarea es totalmente libre, lo importante es la originalidad y el entendimiento de los resultados así como su explicación. Puede seguir el siguiente guion  para la realización:

1 - Grafique las variables implicadas de las maneras que crea oportunas.

2 - Identifique si es necesaria una limpieza de datos y/o completar valores perdidos.

3 - Obtenga las correlaciones entre variables y analice si se pueden observar algunas relaciones interesantes.

4 - Grafique todo lo que considere oportuno.

5 - (Opcional) Aplique algún tipo de clustering o reducción de dimensionalidad e intente encontrar relaciones entre los datos.

Se evaluará la originalidad y la evaluación de los resultados. Lo más importante no es el código, es que los gráficos sean representativos, se puedan entender, y se explique dentro  del archivo de python cada resultado obtenido.

*** Entregue sólo el fichero python (no el dataset) con todos los resultados escritos sobre el mismo.
## Solución propuesta
Para realizar el análisis lo primero que he hecho ha sido importar las librerías necesarias de cara a poder trabajar con los datos. Posteriormente he creado una función que se ejecutará posteriormente dentro de un bucle for para todas las variables numéricas del dataset, en ella podemos ver como obtenemos la media, desviación típica y la mediana, también los valores máximos y mínimos de cada variable.

He podido ver cómo la antiguedad de las casas, su tamaño y su número de habitaciones influían de forma notoria en el precio de las mismas. Por lo que he visto no hay casas realmente cotizadas con edad menor a 3 años, la antiguedad de la más cara es de 7.7 años y el tamaño y número de habitaciones por lo general son directamente proporcionales a los precios. Las casas con antiguedad inferior a la media tienen un precio medio inferior al de las que superan esa edad media de 6 años.

El código empleado para resolverlo es el siguiente: 
```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv("USA_Housing.csv")
print(df)

print("Las columnas del dataset son :\n", df.columns)
print("La descripción del dataset es la siguiente: \n", df.describe())

# calcula la media , mediana, desviación estándar y el valor máximo y mínimo
def analisis(dataset,var):    
    print(f"La media de la columna {var} es: ", dataset[var].mean())
    print(f"La mediana de la columna {var} es: ", dataset[var].median())
    print(f"La desviación estándar de la columna {var} es: ", dataset[var].std())
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
    analisis(df,i)
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
# relaciona precio y antiguedad
plt.figure(figsize=(10,10))
plt.scatter(df['Price'], df['Avg. Area House Age'])
plt.xlabel('Precio de la vivienda')
plt.ylabel('Edad')
plt.show()
# este print devuelve la antiguedad de la casa con mayor precio
print("La antigüedad de la casa con mayor precio es: ", df['Avg. Area House Age'][df['Price'].idxmax()])
# obtengo df2 que contiene casas con antiguedad inferior a 6 años
df2 = df[df['Avg. Area House Age'] < 6]
# halla el precio medio de las casas con antiguedad menor que 6
lista2 = []
for i in df2.columns:
    if df2[i].dtype == np.int64 or df2[i].dtype == np.float64:
        lista2.append(i)
# llamamos a analisis para cada columna
for i in lista2:
    analisis(df2,i)
```
