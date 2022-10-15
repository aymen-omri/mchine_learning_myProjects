from sys import displayhook
import pandas as pd

data = {
    "state":["tunis","bizerte","sfax","sousse","gabes"],
    "year":[2000,2001,2002,2001,2002],
    "pop":[1.5,1.7,3.6,2.4,2.9]
}

df = pd.DataFrame(data)
print(df.info())
displayhook(df)
print(df.columns.tolist())
print(data["year"])

df["pop"] = 5.5 

df["zone"]=""

df1 = df.rename(columns={"state":"A","year":"B","pop":"C","zone":"D"})

df2 = df1.drop(labels="A", axis=1)

print(df2)