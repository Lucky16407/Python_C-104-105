import pandas as pd
import plotly.express as px
import csv

df = pd.read_csv("class1.csv")

with open("class1.csv", newline= '') as f:
    reader = csv.reader(f)
    file_data = list(reader)

file_data.pop(0)
total_marks = 0
total_entries = len(file_data)
for marks in file_data:
    total_marks += float(marks[1])

mean = total_marks/total_entries
print("The Average Marks Of This Class Is: " + str(mean))
figure = px.scatter(df, x = "Student Number", y = "Marks")

figure.update_layout(shapes = [
    dict(
        type = "line",
        y0 = mean, y1 = mean,
        x0 = 0, x1 = total_entries
    )
])

figure.show()