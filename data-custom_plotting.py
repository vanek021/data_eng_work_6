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
need_dtypes = read_types("./data/custom/dtypes.json")
dataset = pd.read_csv("./data/custom/df_sub.csv", usecols=lambda x: x in need_dtypes.keys(), dtype=need_dtypes)

# График 1. Гистограмма по дням
#plt.figure(figsize=(15,10))
#zero_age = dataset[dataset["Vict Age"] == 0]
#dataset = dataset.drop(zero_age.index)
#plot = dataset['Vict Age'].value_counts().plot(kind='bar', title='Гистограмма по возрасту жертв')
#plot.figure.savefig("./data/custom/plots/plot1.png")

# График 2. Скатерограмма по признаку Vict Descent
#fig = plt.figure(figsize=(15,15))
#sns.pairplot(data = dataset,
#             hue ='Vict Descent',
#             palette = 'bwr',).savefig("./data/custom/plots/plot2.png")

# График 3. Гистограмма
plt.figure(figsize=(25,15))
plot = dataset['Weapon Desc'].value_counts().loc[lambda x : x > 1500].plot(kind='bar', title='weapon desc')
plot.figure.savefig("./data/custom/plots/plot3.png")

# График 4. 
#copy = dataset.copy()
#copy.pop('Status')
#copy.pop("Weapon Desc")
#copy.pop("Premis Desc")
#copy.pop('Vict Descent')
#copy.pop("Vict Sex")

#copy_corr = copy.corr()
#sns.heatmap(copy_corr, annot=True)
#plt.savefig("./data/custom/plots/plot4.png")


# График 5. Скатерограмма по признаку
#fig = plt.figure(figsize=(15,15))
#sns.pairplot(data = dataset,
#             hue ='Vict Age',
#             palette = 'bwr',).savefig("./data/custom/plots/plot5.png")