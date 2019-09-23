import os

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Note: This is already manually cleaned file!
path = os.path.join("data","car396 (1).txt")

def get_split(values):
    """This splits arrays on spikes. This is needed to properly draw plots with separations without connecting lines
    e.g. 1-10, 20-29 would give us straight line between 10 and 20, we'd want to split this in two series.
    :param values:
    :return:
    """
    # find the difference between each numbers
    diff_values = np.diff(values)
    # find the index whose difference is more than 2 (we actually need 1 but still)
    split_index = np.where(diff_values > 2)[0]
    # add 1 to index values
    split_index += 1
    # result
    split_values = np.split(values, split_index)
    return split_values


df = pd.read_csv(path)

red = df["LINE_TYPE"] == "DOUBLE"
dotted = df["LINE_TYPE"] == "INTERRUPT"
blue = df["LINE_TYPE"] == "SINGLE"

split_dotted = get_split(df.loc[dotted].index.values)
split_red = get_split(df.loc[red].index.values)
split_blue =get_split(df.loc[blue].index.values)

# We'd want to see something
plt.figure(figsize=(20,20), dpi=100)

for range in split_red:
    plt.plot(range, df.loc[range]["LINE"], "r", df.loc[range]["CAR"], "g")
for range in split_dotted:
    plt.plot(range, df.loc[range]["LINE"], "r--", df.loc[range]["CAR"], "g")
for range in split_blue:
    plt.plot(range, df.loc[range]["LINE"], "b", df.loc[range]["CAR"], "g")

plt.savefig("out.png")
plt.show()

print("Look at the picture out.png")
