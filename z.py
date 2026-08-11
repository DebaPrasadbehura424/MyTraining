import pandas as pd

data = pd.read_csv("car-sales-missing-data.csv")

df = pd.DataFrame(data)

# Missing values fill
df["Make"] = df["Make"].fillna("Honda")
df["Colour"] = df["Colour"].fillna("Red")
df["Odometer"] = df["Odometer"].fillna(100)
df["Doors"] = df["Doors"].fillna(100)
df["Price"] = df["Price"].fillna(100)

print(df)


# df=df.fillna(1);
# print(df.dropna())
# print(df["make"])

# print(df.head());
# print(df.tail());
# print(df.info());
# print(df.index);
# print(df.describe());


# print(df["oddometer"].mean())
# print(df["oddometer"].std())
# print(df["oddometer"].var())
# print(df.sum())
# print(len(df))'

# print(df.loc[0:3])


# print(df["make"]=="Honda")
# print(df["oddometer"]<5000)
# print(df.groupby("make").sum())
# print(pd.crosstab(data["make"],data["door"]))
# print(df["door"].plot())
# print(df["oddometer"].plot())
# print(df["oddometer"].hist())
# print(df["make"].str.lower())





