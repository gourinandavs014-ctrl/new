import pandas as pd

data = {
    "Name": ["anu", "manu", "vinu", "chin", "priya", "ben", "kiran", "mary"],
    "Marks": [34, 45, 56, 78, 67, 89, 54, 34,]
}
df = pd.DataFrame(data)

print(df)

print(df.loc[0])




