import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv("USA_Housing.csv")
print(df)

print("Las columnas del dataset son :\n", df.columns)
print("La descripción del dataset es la siguiente: \n", df.describe())

def media(col):
    return df[col].mean()
def desviacion(col):
    return df[col].std()
def moda(col):
    return df[col].mode()