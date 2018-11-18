from objectStructure import *
from initData import *

import pandas as pd


file = pd.ExcelFile("NBA.xlsx")

data_main = pd.read_excel(file, usecols="C:BC", skiprows=[0, 1, 2, 3, 4, 5])

data_partial = pd.read_excel(file, usecols="F:AD", skiprows=[0, 1, 2, 3, 4, 5])


def replace_zero(value):
    value_string = value.astype(str)
    if value_string.equals('-'):
        return 0
    elif value.astype(str)[:-1].equals('%'):
        return value_string[0:len(value_string)-1]
    return value


data_main.apply(replace_zero)

data_partial.apply(replace_zero)

teams = initialize_data(data_main)

print(teams["Heatcheck Gaming"].players["24KDropOff"].tip_off.blk)
