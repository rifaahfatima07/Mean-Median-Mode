import pandas as pd
import statistics

df = pd.read_csv("data.csv")
data = df["Height(Inches)"].tolist()

mean = statistics.mean(data)
median = statistics.median(data)
mode = statistics.mode(data)
print(mean, median, mode)