import pandas as pd
import csv
import plotly.graph_objects as go

data = pd.read_csv("data.csv")
stu = data.loc[data['student_id']=="TRL_zet"]
print(stu.groupby("level")["attempt"].mean())

graph = go.Figure(go.Scatter(
    x=stu.groupby("level")["attempt"].mean(),
    y=['Level1','Level2','Level3','Level4'],
    orientation = 'h'))
graph.show()
