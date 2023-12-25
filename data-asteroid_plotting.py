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
need_dtypes = read_types("./data/asteroid/dtypes.json")
dataset = pd.read_csv("./data/asteroid/df_sub.csv", usecols=lambda x: x in need_dtypes.keys(), dtype=need_dtypes)

# График 1. Гистограмма по class
#plot = dataset['class'].value_counts().plot(kind='bar', title='class')
#plot.figure.savefig("./data/asteroid/plots/plot1.png")

# График 2. Скатерограмма по признаку albedo
#fig = plt.figure(figsize=(15,15))
#sns.pairplot(data = dataset,
#             hue ='albedo',
#             palette = 'bwr',).savefig("./data/asteroid/plots/plot2.png")


# График 3
#plt.figure(figsize=(20, 10))
#plot = dataset['orbit_id'].value_counts().loc[lambda x : x > 2000].plot(kind='bar', title='class')
#plt.title("orbit_id")
#plot.figure.savefig("./data/asteroid/plots/plot3.png")

# График 4. 
#copy = dataset.copy()
#copy.pop('class')
#copy.pop("orbit_id")
#copy.pop("equinox")
#copy.pop("name")
#copy.pop("pdes")
#copy.pop("id")

#copy_corr = copy.corr()
#sns.heatmap(copy_corr, annot=True)
#plt.savefig("./data/asteroid/plots/plot4.png")


# График 5. Скатерограмма по признаку equinox
fig = plt.figure(figsize=(15,15))
sns.pairplot(data = dataset.sample(100000),
             hue ='albedo',
             palette = 'bwr',).savefig("./data/asteroid/plots/plot5.png")