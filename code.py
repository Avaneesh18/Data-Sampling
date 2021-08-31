import plotly.figure_factory as ff
import plotly.graph_objects as go
import statistics 
import pandas as pd
import random
import csv

ef = pd.read_csv("newdata1.csv")
data = ef["average"].tolist()

fig = ff.create_distplot([data],["average"], show_hist = False)
fig.show()

datset = []
for i in range(0,100):
  randomindex = random.randint(0,len(data)) 
  val = data[randomindex]
  datset.append(val)

mean = statistics.mean(datset)
stdv = statistics.stdev(datset)

print("Mean is: ",mean)
print("Standeard deviation is :",std)

def randomsetofmean(counter):
  datset = []
  for i in range(0,counter):
    randomindex = random.randint(0,len(data)-1) 
    val = data[randomindex]
    datset.append(val)

  mean = statistics.mean(datset)
  return mean

def showfig(meanlist):
  ef = meanlist
  mean = statistics.mean(ef)
  fig = ff.create_distplot([ef],["average"], show_hist = False)
  fig.add_trace(go.Scatter(x = [mean,mean], y = [0,1], mode = "lines", name = "MEAN"))
  fig.show()

def setup():
  meanlist = []
  for i in range(0,1000):
    setofmean = randomsetofmean(100) 
    meanlist.append(setofmean)
  showfig(meanlist)

  mean = statistics.mean(meanlist)
  print("Mean is : ",mean)

setup()

popumean = statistics.mean(data)

print("Population mean is: ",popumean)

def std():
  meanlist = []
  for i in range(0,1000):
    setofmean = randomsetofmean(100)
    meanlist.append(setofmean)

  stdv = statistics.stdev(meanlist)
  print("Standeard deviation is: ",stdv)

std()