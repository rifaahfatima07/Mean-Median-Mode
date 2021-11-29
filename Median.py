import pandas as pd

df = pd.read_csv("data.csv")
data = df["Height(Inches)"].tolist()

number = len(data)
print(number)

print(data[0])
data.sort()
print(data[0])

mid1 = data[int (number/2-1)]
mid2 = data[int (number/2)]

median =( mid1 + mid2)/2
print(median)

