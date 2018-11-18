from getData import *
import pandas as pd

file = pd.ExcelFile("NBA.xlsx")

data = pd.read_excel(file, usecols="C:BC", skiprows=[0, 1, 2, 3, 4, 5])


def initialize_data(dataframe):
    teams_dic = {}
    data_list = dataframe.values
    for entry in data_list:
        if entry[0] in teams_dic:
            teams_dic[entry[0]].add_player(entry)
        else:
            teams_dic[entry[0]] = Team(entry[0])
            teams_dic[entry[0]].add_player(entry)
    return teams_dic


teams = initialize_data(data)
print(teams["Heatcheck Gaming"].players["24KDropOff"].tip_off.pts)
