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
need_dtypes = read_types("./data/game_logs/dtypes.json")
dataset = pd.read_csv("./data/game_logs/df_sub.csv", usecols=lambda x: x in need_dtypes.keys(), dtype=need_dtypes)

# График 1. Гистограмма по дням
#plt.figure(figsize=(30,5))
#sort_dow = dataset['day_of_week'].sort_index()
#plot = sort_dow.hist()
#plot.get_figure().savefig("./data/game_logs/plots/plot1.png")

# График 2. Скатерограмма по признаку park_id
#fig = plt.figure(figsize=(15,15))
#sns.pairplot(data = dataset,
#             hue ='park_id',
#             palette = 'bwr',).savefig("./data/game_logs/plots/plot2.png")


# График 3. Гистограмма по продолжительности
#plt.figure(figsize=(15,15))
#plot = dataset["length_minutes"].hist()
#plot.get_figure().savefig("./data/game_logs/plots/plot3.png")

# График 4. 
#copy = dataset.copy()
#copy.pop('day_of_week')
#copy.pop("park_id")
#copy.pop("v_manager_name")

#copy_corr = copy.corr()
#sns.heatmap(copy_corr, annot=True)
#plt.savefig("./data/game_logs/plots/plot4.png")


# График 5. Скатерограмма по признаку v_manager_name
fig = plt.figure(figsize=(15,15))
sns.pairplot(data = dataset,
             hue ='v_manager_name',
             palette = 'bwr',).savefig("./data/game_logs/plots/plot5.png")