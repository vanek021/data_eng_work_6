import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import utils
import json

pd.set_option("display.max_rows", 20, "display.max_columns", 60)

def read_types(file_name):
    dtypes = dict()
    with open(file_name, mode="r") as file:
        dtypes = json.load(file)

    for key in dtypes.keys():
        if dtypes[key] == 'category':
            dtypes[key] = pd.CategoricalDtype
        else:
            dtypes[key] = np.dtype(dtypes[key])

    return dtypes

#9. Используя оптимизированный набор данных, построить пять-семь графиков (включая разные типы: линейный, столбчатый, круговая диаграмма, корреляция и т.д.)
need_dtypes = read_types("./data/automotive/dtypes.json")
dataset = pd.read_csv("./data/automotive/df_sub.csv", usecols=lambda x: x in need_dtypes.keys(), dtype=need_dtypes)

# График 1. Гистограмма по brandName
#plt.figure(figsize=(25,15))
#plot = dataset['brandName'].value_counts().loc[lambda x : x > 1500].plot(kind='bar', title='brandName')
#plot.figure.savefig("./data/automotive/plots/plot1.png")

# График 2. Гистограмма по modelName
#plt.figure(figsize=(25,15))
#plot = dataset['modelName'].value_counts().loc[lambda x : x > 1500].plot(kind='bar', title='modelName')
#plot.figure.savefig("./data/automotive/plots/plot2.png")

# График 3. Гистограмма по color
#plt.figure(figsize=(25,15))
#plot = dataset['color'].value_counts().loc[lambda x : x > 1500].plot(kind='bar', title='color')
#plot.figure.savefig("./data/automotive/plots/plot3.png")

# График 4. Гистограмма по interiorColor
#plt.figure(figsize=(25,15))
#plot = dataset['interiorColor'].value_counts().loc[lambda x : x > 1500].plot(kind='bar', title='interiorColor')
#plot.figure.savefig("./data/automotive/plots/plot4.png")


# График 5.
plt.figure(figsize=(10,10))
dataset_copy = dataset.copy(deep=True)
dataset_copy = dataset_copy.sort_values(by = "mileage")
d1 = dataset_copy['mileage']
d2 = dataset_copy['askPrice']
plt.plot(d1, d2, color='green') 
plt.savefig("./data/automotive/plots/plot5.png") 