import pandas as pd

data=pd.read_csv("C:/Users/debap/OneDrive/Desktop/class/data.csv")
df=pd.DataFrame(data)
desc=df.describe()
h=df.head(1)
t=df.tail()


# print(desc)
# print(h)
# print(t)

# print(df.info())

print(df.loc[0])
print("break")
print(df.iloc[1])