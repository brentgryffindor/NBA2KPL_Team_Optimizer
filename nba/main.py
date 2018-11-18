from objectStructure import *
from initData import *
from getWeight import *

import pandas as pd


file = pd.ExcelFile("NBA.xlsx")

data_main = pd.read_excel(file, usecols="C:BC", skiprows=[0, 1, 2, 3, 4, 5])

data_partial = pd.read_excel(file, usecols="F:AD", skiprows=[0, 1, 2, 3, 4, 5])


def replace_zero(value):
    value_string = value.astype(str)
    if pd.Series.to_string(value) == '-':
        print("la")
        return 0
    elif value.astype(str)[:-1].equals('%'):
        return float(value_string[0:len(value_string)-1])
    return value


print(data_main('9')['J'])

data_main.apply(replace_zero)

data_partial.apply(replace_zero)

teams = initialize_data(data_main)

#get_training_set(data_partial)

#print(data_partial)

print(teams["Heatcheck Gaming"].players["24KDropOff"].play_off.ast_to_ratio)
