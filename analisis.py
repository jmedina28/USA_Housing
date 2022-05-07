import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv("USA_Housing.csv")
print(df)

print("Las columnas del dataset son :\n", df.columns)
print("La descripción del dataset es la siguiente: \n", df.describe())