import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv("data.csv", index_col=0, header=None)
print(df.head())
print(df.describe())

plt.hist(df[1].tolist(), bins=100)
plt.savefig("2_graph.png")
plt.title("Distribution of Sample Data")
plt.xlabel("Value")
plt.ylabel("Frequency")
plt.savefig("2_graph.png")
plt.show(block=False)

# 