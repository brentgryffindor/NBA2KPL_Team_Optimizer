from objectStructure import *
from initData import *

import pandas as pd


file = pd.ExcelFile("NBA.xlsx")

data = pd.read_excel(file, usecols="C:BC", skiprows=[0, 1, 2, 3, 4, 5])

teams = initialize_data(data)



print(teams["Heatcheck Gaming"].players["24KDropOff"].pos)
