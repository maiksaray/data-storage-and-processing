import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


def exp_smooth(arr, alpha):
    prev = None
    for curr in arr:
        prev = prev + alpha * (curr - prev) if prev else curr
        yield prev


data = np.array([42, 41, 45, 38, 52, 53, 50, 48, 44, 60, 61, 54, 51, 49, 59, 55, 63, 68, 69, 62])

plt.plot(data)
plt.show()

smoothed = np.array(list(exp_smooth(data, alpha=0.23)))

plt.plot(smoothed)
plt.show()

print(smoothed)
