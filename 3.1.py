import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data_path = os.path.join("data", "vasya.txt")

data = pd.read_csv(data_path, sep=";", encoding="utf-8")

data = data.set_index("ID")


def normalize(df):
    result = df.copy()
    for feature_name in df.columns:
        max_value = df[feature_name].max()
        min_value = df[feature_name].min()
        result[feature_name] = (df[feature_name] - min_value) / (max_value - min_value)
    return result


def exp_norm(df):
    result = df.copy()
    for feature_name in df.columns:
        min = df[feature_name].min()
        result[feature_name] = 1 - np.exp(1 - df[feature_name] / min)
    return result


# get normalized values for each column
normal = normalize(data)
exp_normal = exp_norm(data)

# Get sum of values for each row
summed = normal.sum(axis=1)

exp_summed = exp_normal.sum(axis=1)

# If you want to see how different normalizations work - uncomment these.
# plt.plot(summed)
# plt.show()
#
# plt.plot(exp_summed)
# plt.show()

# Get first three indecies
result = summed.sort_values()[:3]

exp_result = exp_summed.sort_values()[:3]
print(result.index)
print(exp_result.index)
