import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("avg.csv")

print(df)

plt.pie(df["total"], labels=df["students"])
plt.title("Students total marks")

plt.show()
