import plotly_express as pe
import numpy as np
import csv

def getdatasource(datapath):
    pre = []
    marks = []

    with open("4th.csv") as f:
        reader = csv.DictReader(f)
        for row in reader:
            pre.append(float(row["pre"]))
            marks.append(float(row["marks"]))
        return{"x":pre,"y":marks}

def findcorrelation(datasource):
    correlation = np.corrcoef(datasource["x"],datasource["y"])
    print(correlation[0,1])

def main():
    datapath = "4th.csv"
    datasource = getdatasource(datapath)
    findcorrelation(datasource)

main()