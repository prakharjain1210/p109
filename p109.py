from csv import reader
import statistics
import plotly.graph_objects as go
import pandas as pd
import plotly.figure_factory as ff

read=pd.read_csv("data109.csv")
math_score=read["math score"].tolist()

mean=statistics.mean(math_score)
median=statistics.median(math_score)
mode=statistics.mode(math_score)
std_dev=statistics.stdev(math_score)

print("mean is:", mean)
print("mediam is:",median)
print("mode is:",mode)
print("standard deviation is:",std_dev)

first_std_start,first_std_end=mean-std_dev,mean+std_dev
second_std_start,second_std_end=mean-(2*std_dev),mean+(2*std_dev)
third_std_start,third_std_end=mean-(3*std_dev),mean+(3*std_dev)

fig=ff.create_distplot([math_score],["marks"],show_hist=False)
fig.add_trace(go.Scatter(x=[mean,mean],y=[0,0.17],mode="lines",name="MEAN"))
fig.add_trace(go.Scatter(x=[first_std_start,first_std_start],y=[0,0.17],mode="lines",name="first_std_start"))
fig.add_trace(go.Scatter(x=[first_std_end,first_std_end],y=[0,0.17],mode="lines",name="first_std_end"))
fig.add_trace(go.Scatter(x=[second_std_start,second_std_start],y=[0,0.17],mode="lines",name="second_std_start"))
fig.add_trace(go.Scatter(x=[second_std_end,second_std_end],y=[0,0.17],mode="lines",name="second_std_end"))
fig.add_trace(go.Scatter(x=[third_std_start,third_std_start],y=[0,0.17],mode="lines",name="third_std_start"))
fig.add_trace(go.Scatter(x=[third_std_end,third_std_end],y=[0,0.17],mode="lines",name="third_std_end"))
fig.show()