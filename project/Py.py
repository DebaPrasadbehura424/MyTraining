import pandas as pd;

data=pd.read_csv("project/ola.csv");

df= pd.DataFrame(data)

print(df.head(3));
# print(df.shape);
# print(df[["datetime", "temp", "humidity","count"]]);
# print(df[["count"]].max());
# print(df["count"].max());
# print(df["temp"].mean());
# print(df[["humidity"]]>80);

# print(df[["count"]]>50);
print(df[["season"]].mean());