import pandas as pd
import csv 
import plotly.express as pe
import numpy as np

def getdatasource(datapath):
    temp = []
    icecreamsales = []

    with open("temp_icecream.csv") as f:
        reader = csv.DictReader(f)
        for row in reader:
            temp.append(float(row["temp"]))
            icecreamsales.append(float(row["icecreamsales"]))
        return{"x":temp,"y":icecreamsales}

def findcorrelation(datasource):
    correlation = np.corrcoef(datasource["x"],datasource["y"])
    print(correlation[0,1])

def main():
    datapath = "temp_icecream.csv"
    datasource = getdatasource(datapath)
    findcorrelation(datasource)

main()