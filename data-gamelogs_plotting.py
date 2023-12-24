import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import utils
import json
import datetime

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
#plt.figure(figsize=(10,10))
#plot = dataset['day_of_week'].value_counts().plot(kind='bar', title='Частота по определенным дням')
#plot.figure.savefig("./data/game_logs/plots/plot1.png")

# График 2. Скатерограмма по признаку day_of_week
#fig = plt.figure(figsize=(15,15))
#sns.pairplot(data = dataset,
#             hue ='day_of_week',
#             palette = 'bwr',).savefig("./data/game_logs/plots/plot2.png")

# График 3. Гистограмма по продолжительности
#plt.figure(figsize=(10,10))
#dataset_copy = dataset.copy(deep=True)
#dataset_copy["year"] = dataset_copy.apply(pd.to_datetime(dataset_copy["date"]).dt.tz_localize("UTC"), axis=1)
#dataset_copy = dataset_copy.assign(day=lambda df: pd.to_datetime(df["date"], unit='s').dt.day)
#gr_obj = dataset_copy.groupby(["day"])['length_minutes'].mean()
#plt.plot(gr_obj.index, gr_obj.values, color='green') 
#plt.xticks(range(1, 31))
#plt.title("Games in august by duration and date of month") 
#plt.savefig("./data/game_logs/plots/plot3.png") 

# График 4. 
#plt.figure(figsize=(15,15))
#copy = dataset.copy()
#copy.pop('day_of_week')
#copy.pop("park_id")
#copy.pop("v_manager_name")
#copy_corr = copy.corr()
#sns.heatmap(copy_corr, annot=True)
#plt.savefig("./data/game_logs/plots/plot4.png")


# График 5. Скатерограмма по признаку v_manager_name
#fig = plt.figure(figsize=(15,15))
#sns.pairplot(data = dataset,
#             hue ='v_manager_name',
#             palette = 'bwr',).savefig("./data/game_logs/plots/plot5.png")