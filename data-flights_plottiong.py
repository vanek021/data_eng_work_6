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
need_dtypes = read_types("./data/flights/dtypes.json")
dataset = pd.read_csv("./data/flights/df_sub.csv", usecols=lambda x: x in need_dtypes.keys(), dtype=need_dtypes)

# График 1. Гистограмма по дням
#plt.figure(figsize=(15,10))
#plot = dataset['DAY_OF_WEEK'].value_counts().plot(kind='bar', title='Количество вылетов по дням недели')
#plot.figure.savefig("./data/flights/plots/plot1.png")

# График 2. Гистограмма по авиакомпаниям
#plt.figure(figsize=(15,10))
#plot = dataset['AIRLINE'].value_counts().plot(kind='bar', title='Гистограмма по авиакомпаниям')
#plot.figure.savefig("./data/flights/plots/plot2.png")

# График 3. График зависимости суммарной задержки вылета от 
#dataset = dataset.assign(DEPARTURE_DELAY=lambda x: x.DEPARTURE_TIME - x.SCHEDULED_DEPARTURE).loc[lambda x : x.DEPARTURE_DELAY >=1]
#gr_obj = dataset.groupby(["DAY_OF_WEEK"])['DEPARTURE_DELAY'].mean()
#plt.plot(gr_obj.index, gr_obj.values, color='green') 
#plt.xticks(range(1, 7))
#plt.title("Задержки вылета в зависимости от дня недели") 
#plt.savefig("./data/flights/plots/plot3.png") 

# График 4. Корреляция числовых данных
#plt.figure(figsize=(15,15))
#copy = dataset.copy(deep=True)
#copy.pop('TAIL_NUMBER')
#copy.pop("AIRLINE")
#copy.pop("DESTINATION_AIRPORT")
#copy.pop("ORIGIN_AIRPORT")
#copy_corr = copy.corr()
#sns.heatmap(copy_corr, annot=True)
#plt.title("Корреляция числовых данных")
#plt.savefig("./data/flights/plots/plot4.png")

# График 5. Скатерограмма по признаку AIRLINE
#fig = plt.figure(figsize=(15,15))
#sns.pairplot(data = dataset,
#             hue ='AIRLINE',
#             palette = 'bwr',).savefig("./data/flights/plots/plot5.png")