from getData import *
import pandas as pd

file = pd.ExcelFile("NBA.xlsx")

data = pd.read_excel(file, usecols="C:BC", skiprows=[0, 1, 2, 3, 4, 5])

print(data.values)

heatcheck_gaming = Team("Heatcheck Gaming")
raptors_uprising_gc = Team("Raptors Uprising GC")
celtics_crossover_gaming = Team("Celtics Crossover Gaming")
grizz_gaming = Team("Grizz Gaming")
mavs_gaming = Team("Mavs Gaming")
bucks_gaming = Team("Bucks Gaming")
wizards_district_gaming = Team("Wizards District Gaming")
warriors_gaming_squad = Team("Warriors Gaming Squad")
kings_guard_gaming = Team("Kings Guard Gaming")
blazers_gaming = Team("Blazers Gaming")
jazz_gaming = Team("Jazz Gaming")
pacers_gaming = Team("Pacers Gaming")
cavs_legion_gc = Team("Cavs Legion GC")
knicks_gaming = Team("Knicks Gaming")
seven_sixers_gc = Team("76ers GC")
pistons_gt = Team("Pistons GT")
magic_gaming = Team("Magic Gaming")


def contains(team_list, name):
    for team in team_list:
        if team.name == name:
            return True
    return False


teams = []
