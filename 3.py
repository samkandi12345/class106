from numpy.lib.function_base import corrcoef
import plotly.express as pe
import csv
import numpy as np

def getdatasource(datapath):
    sizeoftv = []
    time = []

    with open("avg.csv") as f:
        reader = csv.DictReader(f)
        for row in reader:
            sizeoftv.append(float(row["size"]))
            time.append(float(row["time"]))
        return{"x":sizeoftv,"y":time}

def findcorrelation(datasource):
    correlation = np.corrcoef(datasource["x"],datasource["y"])
    print(correlation[0,1])

def main():
    datapath = "avg.csv"
    datasource = getdatasource(datapath)
    findcorrelation(datasource)

main()