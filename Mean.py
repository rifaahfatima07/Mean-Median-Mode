import pandas as pd

df = pd.read_csv("data.csv")
data = df["Height(Inches)"].tolist()

number = len(data)
sum = 0
for v in data:
    sum = sum + v
    
average = sum/number
print(average)
