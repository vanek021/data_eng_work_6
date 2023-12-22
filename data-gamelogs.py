import pandas as pd
import matplotlib
import numpy as np
import utils

pd.set_option("display.max_rows", 20, "display.max_columns", 60)

file_name = "./data/game_logs/game_logs.csv"

# 1. Загрузить набор данных из файла
dataset = utils.read_file(file_name)

#2.	Провести анализ набора данных по следующим параметрам:
    #a.	Объем памяти, который занимает файл на диске
    #b.	Объем памяти, который занимает набор данных при загрузке в память
    #c.	Вычислить для каждой колонки занимаемый объем памяти, долю от общего объема, а также выяснить тип данных
#3.	Полученный набор данных отсортировать по занимаемому объему памяти
# Вывести в файл (json) данные по колонкам с пометкой, что это статистика по набору данных без применения оптимизаций.
utils.handle_file_size(dataset, file_name, "./data/game_logs/file_size_unopt_result.json")

#4.	Преобразовать все колонки с типом данных «object» в категориальные, если количество уникальных значений колонки составляет менее 50%.
#5.	Провести понижающее преобразование типов «int» колонок 
#6.	Провести понижающее преобразование типов «float» колонок
optimized_dataset = dataset.copy()

converted_obj = utils.opt_obj(dataset)
converted_int = utils.opt_int(dataset)
converted_float = utils.opt_float(dataset)

# 7. Повторно провести анализ набора данных, как в п. 2, сравнив показатели занимаемой памяти
optimized_dataset[converted_obj.columns] = converted_obj
optimized_dataset[converted_int.columns] = converted_int
optimized_dataset[converted_float.columns] = converted_float

utils.handle_file_size(optimized_dataset, file_name, "./data/game_logs/file_size_opt_result.json")

#8.	Выбрать произвольно 10 колонок для дальнейшем работы, прописав преобразование типов и загрузку только нужных данных на этапе чтения файла. 
# При этом стоит использовать чанки. Сохраните полученный поднабор в отдельном файле.

need_column = dict()
opt_dtypes = optimized_dataset.dtypes

column_names = ['date', 'number_of_game', 'day_of_week',
                'park_id', 'v_manager_name', 'length_minutes',
                'v_hits', 'h_hits', 'h_walks', 'h_errors']
for key in column_names:
    need_column [key] = opt_dtypes[key]
    print(f" {key}: {opt_dtypes [key]}")

has_header = True
for chunk in pd.read_csv(file_name, usecols=lambda x: x in column_names, dtype=need_column, chunksize=100_000):
    print(utils.mem_usage(chunk))
    chunk.to_csv("./data/game_logs/df_sub.csv", mode="a", header=has_header)
    has_header = False

dtype_json = need_column.copy()
for key in dtype_json.keys():
    dtype_json[key] = str(dtype_json[key])
utils.write_to_json("./data/game_logs/dtypes.json", dtype_json)
