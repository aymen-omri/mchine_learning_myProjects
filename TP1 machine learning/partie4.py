import csv
import pandas as pd 

df = pd.read_csv("./pima-indians-diabetes.data.csv")


df.columns = ["NumTimesPrg","PlGlcConc","BloodP","SkinThick","TwoHourSerIns","BMI","DiPedFunc","age","HasDiabetes"]
print(df)

