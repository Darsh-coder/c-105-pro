import csv
import pandas as pd
import plotly.express as px

with open("ad.csv",newline="")as f:
    reader = csv.reader(f)
    filedata = list(reader)


filedata.pop(0)

totalent = len(filedata)
totalmarks = 0

for marks in filedata :
    totalmarks += float(marks[1])

mean = totalmarks/totalent

print(mean)

df = pd.read_csv("ad.csv")


fig = px.scatter(df , x = "Student Number" , y ="Marks")

fig.update_layout(shapes=[dict(type = "line",y0 = mean , y1 =mean,x0 =0 ,x1 = totalent)])

fig.update_yaxes(rangemode = 'tozero')

fig.show()



























