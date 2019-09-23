import os
import pandas as pd
import numpy as np

data_path = os.path.join("data", "Бакалавры_final.csv")

data = pd.read_csv(data_path, sep=";", encoding="utf-8")

points = data.loc[:, 'Упражнение 1: Упражнение. Архитектура ЭВМ и ОС':'Эссе']

weights = np.array([(0.8 / 15)] * 15 + [0.2])

data["Total"] = np.sum((points * weights), axis=1)

groupby = data.groupby("Группа")
total_avg = groupby["Total"].mean()
counts = groupby["student_id"].count()

task_columns = [
    'Упражнение 1: Упражнение. Архитектура ЭВМ и ОС',
    'Упражнение 2: Упражнение. Технологии программирования',
    'Упражнение 3: Упражнение. Сетевые технологии',
    'Упражнение 4: Упражнение. Цифровая этика',
    'Упражнение 5: Упражнение. Технологии виртуальной дополненной и смешанной реальности',
    'Упражнение 6: Упражнение. Информационная безопасность',
    'Упражнение 7: Упражнение. Технологии Интернета и WEB',
    'Упражнение 8: Упражнение. Цифровая экономика. Блокчейн',
    'Упражнение 9: Упражнение. Основы персональной информационной безопасности',
    'Упражнение 10: Упражнение. Встроенные системы',
    'Упражнение 11: Упражнение. Квантовые технологии',
    'Упражнение 12: Упражнение. Умные вещи и/или безопасная жизнь',
    'Упражнение 13: Упражнение. Культура Интернет-коммуникаций',
    'Упражнение 14: Упражнение. Цифровое образование',
    'Упражнение 15: Упражнение. Цифровые гуманитарные науки', 'Эссе']

output_table = pd.DataFrame(columns=["Группа"] + task_columns + ["Total", "Size"])

for key in groupby.groups.keys():
    row = {"Группа": key}
    for column in task_columns:
        row[column] = groupby[column].mean()[key]
    row["Total"] = groupby["Total"].mean()[key]
    row["Size"] = groupby["student_id"].count()[key]
    output_table.loc[len(output_table)] = row

# Какой средний балл по Упражнению 1 по всем студентам факультета Низкомтемпературной энергетики
# (первая позиция в номере группы W)?

fst_task = "Упражнение 1: Упражнение. Архитектура ЭВМ и ОС"

W_groups = [item for item in groupby.groups.keys() if item.startswith("W")]

mean_fst = data.loc[data["Группа"].isin(W_groups)][fst_task].mean()

print(mean_fst.round())

# Какая группа на факультете Безопасности информационных технологий (первая позиция в номере группы N)
# хуже всех справилась с упражнением 6 (набрала наименьший средний балл?

sixth_task = "Упражнение 6: Упражнение. Информационная безопасность"

N_groups = [item for item in groupby.groups.keys() if item.startswith("N")]

N_groups_data = output_table.loc[output_table["Группа"].isin(N_groups)]

worst_group = N_groups_data.loc[N_groups_data[sixth_task].idxmin()]

print(worst_group["Группа"])

# Сколько человек выполнило упражнение 9 на 100 баллов?

nineth_task = "Упражнение 9: Упражнение. Основы персональной информационной безопасности"

count_third = data.loc[data[nineth_task] == 100].count()["student_id"]

print(count_third)