from objectStructure import *


def initialize_data(dataframe):
    teams_dic = {}
    data_list = dataframe.values
    for entry in data_list:
        if entry[0] in teams_dic:
            teams_dic[entry[0]].add_player(entry)
        else:
            teams_dic[entry[0]] = Team(entry[0])
            teams_dic[entry[0]].add_player(entry)

    teams_dic["Heatcheck Gaming"].players["Majes7ic"].pos = "PG"
    teams_dic["Heatcheck Gaming"].players["HyperIsPro"].pos = "SG"
    teams_dic["Heatcheck Gaming"].players["Jalen03303"].pos = "SG"
    teams_dic["Heatcheck Gaming"].players["Sharpshooterlos"].pos = "SF"
    teams_dic["Heatcheck Gaming"].players["24KDropOff"].pos = "PF"
    teams_dic["Heatcheck Gaming"].players["Hotshot"].pos = "C"

    teams_dic["76ers GC"].players["ZDS"].pos = "PG"
    teams_dic["76ers GC"].players["Radiant"].pos = "PG"
    teams_dic["76ers GC"].players["Newdini33"].pos = "SG"
    teams_dic["76ers GC"].players["Steez"].pos = "SF"
    teams_dic["76ers GC"].players["Ifeast"].pos = "PF"
    teams_dic["76ers GC"].players["Xtfr3shxx"].pos = "C"

    teams_dic["Blazers Gaming"].players["MamaImDatMan"].pos = "PG"
    teams_dic["Blazers Gaming"].players["GrantMonster"].pos = "SG"
    teams_dic["Blazers Gaming"].players["Lavish_Phenom"].pos = "SF"
    teams_dic["Blazers Gaming"].players["DatBoyShotz"].pos = "PF"
    teams_dic["Blazers Gaming"].players["Jomar12PR"].pos = "C"
    teams_dic["Blazers Gaming"].players["OneWildWalnut"].pos = "C"

    teams_dic["Bucks Gaming"].players["Game6Drake"].pos = "PG"
    teams_dic["Bucks Gaming"].players["Procis1on"].pos = "SG"
    teams_dic["Bucks Gaming"].players["XXSTL2LAXX"].pos = "SF"
    teams_dic["Bucks Gaming"].players["Bigmeek"].pos = "SF"
    teams_dic["Bucks Gaming"].players["KingPeroxide"].pos = "PF"
    teams_dic["Bucks Gaming"].players["OLarry"].pos = "C"

    teams_dic["Cavs Legion GC"].players["Savage"].pos = "PG"
    teams_dic["Cavs Legion GC"].players["Hood"].pos = "PG"
    teams_dic["Cavs Legion GC"].players["Toxsik"].pos = "SG"
    teams_dic["Cavs Legion GC"].players["Godddof2k"].pos = "SF"
    teams_dic["Cavs Legion GC"].players["Turnupdefense"].pos = "PF"
    teams_dic["Cavs Legion GC"].players["SickX973"].pos = "C"

    teams_dic["Celtics Crossover Gaming"].players["Palmoilplease"].pos = "PG"
    teams_dic["Celtics Crossover Gaming"].players["Ofab"].pos = "PG"
    teams_dic["Celtics Crossover Gaming"].players["Profusion"].pos = "SG"
    teams_dic["Celtics Crossover Gaming"].players["MelEast"].pos = "SF"
    teams_dic["Celtics Crossover Gaming"].players["Speedbrook"].pos = "PF"
    teams_dic["Celtics Crossover Gaming"].players["Ars0nalX"].pos = "C"

    return teams_dic
