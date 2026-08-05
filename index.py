import pandas as pd

data=pd.read_csv("C:/Users/debap/OneDrive/Desktop/class/data.csv")
df=pd.DataFrame(data)
desc=df.describe()
h=df.head(1)
# print(desc)
print(h)