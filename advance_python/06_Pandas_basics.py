import pandas as pd
data = {
    "name":["John", "Jane", "Doe","mahesh","ganesh","ramesh","suresh"],
    "marks":[85, 90, 78, 45, 56, 87, 78]
}

df = pd.DataFrame(data)
# print(df.head())
# print(df.tail())
# print(df.describe())

print(df["marks"])