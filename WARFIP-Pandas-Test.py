import pandas as pd
import numpy as np


player_name_input = input('Input player full name.')

player_finder = pd.read_csv('Fill NaN for Final.csv', index_col='Name')
player_finder_rework = player_finder.infer_objects().dtypes
player_info = player_finder.loc[[player_name_input]]



num_PA = player_info['PA']
team_raw = player_info['Team']
team_check = list(team_raw.values)
team = team_check[0]
player_wOBA = player_info['wOBA']


teams_dict = {'COL': ['AL', 1.12], 'CIN': ['NL', 1.12], 'BOS': ['AL', 1.11], 'BAL': ['AL', 1.08], 'KCR': ['AL', 1.08], 'TOR': ['AL', 1.06], 'ATL': ['NL', 1.05],
              'CHC': ['NL', 1.03], 'ARI': ['NL', 1.03], 'MIL': ['NL', 1.02], 'LAA': ['AL', 1.02], 'PIT': ['NL', 1.01], 'CHW': ['AL', 1.00], 'HOU': ['AL', 0.99],
              'MIN': ['AL', 0.99], 'SFG': ['NL', 0.99], 'NYY': ['AL', 0.99], 'TEX': ['AL', 0.98], 'PHI': ['NL', 0.98], 'LAD': ['NL', 0.98], 'CLE': ['AL', 0.97], 'WSN': ['NL', 0.97],
              'MIA': ['NL', 0.97], 'SDP': ['NL', 0.96], 'OAK': ['AL', 0.94], 'DET': ['AL', 0.94], 'SEA': ['AL', 0.94], 'STL': ['NL', 0.92], 'NYM': ['NL', 0.91], 'TBR': ['AL', 0.89]}


def bt_runs(num_PA, team, player_wOBA):
    lg_wOBA = 0.314
    scale_wOBA = 1.209
    lg_run_per_PA = 0.121
    nonP_AL_wRC_per_PA = 0.1225
    nonP_NL_wRC_per_PA = 0.1123
    nonP_neutral_wRC_per_PA = 0.1176
    park_factor = 100
    player_league = ''
    num_bt_runs = 0
    for key, values in teams_dict.items():
        if team in teams_dict.keys():
            team_key = list(teams_dict.get(team))
            player_league = team_key[0]
            park_factor = team_key[1]
    num_wRAA = ((player_wOBA - lg_wOBA) / (scale_wOBA)) * num_PA
    if player_league == 'AL':
        num_bt_runs = num_wRAA + ((lg_run_per_PA - (park_factor * lg_run_per_PA)) * num_PA) + ((lg_run_per_PA - nonP_AL_wRC_per_PA) * num_PA)
    elif player_league == 'NL':
        num_bt_runs = num_wRAA + ((lg_run_per_PA - (park_factor * lg_run_per_PA)) * num_PA) + ((lg_run_per_PA - nonP_NL_wRC_per_PA) * num_PA)
    else:
        num_bt_runs = num_wRAA + ((lg_run_per_PA - (park_factor * lg_run_per_PA)) * num_PA) + ((lg_run_per_PA - nonP_neutral_wRC_per_PA) * num_PA)
    return num_bt_runs

print(bt_runs(num_PA, team, player_wOBA))

#player pos_adj raw numbers
raw_innings_1B = player_info['num_innings_1B'].astype(int)
raw_innings_2B = player_info['num_innings_2B'].astype(int)
raw_innings_3B = player_info['num_innings_3B'].astype(int)
raw_innings_SS = player_info['num_innings_SS'].astype(int)
raw_innings_LF = player_info['num_innings_LF'].astype(int)
raw_innings_CF = player_info['num_innings_CF'].astype(int)
raw_innings_RF = player_info['num_innings_RF'].astype(int)
raw_num_DH_PA = player_info['PA_DH'].astype(int)

#player pos_adj list
new_change = []
new_change.append(list(raw_innings_1B.values))
new_change.append(list(raw_innings_2B.values))
new_change.append(list(raw_innings_3B.values))
new_change.append(list(raw_innings_SS.values))
new_change.append(list(raw_innings_LF.values))
new_change.append(list(raw_innings_CF.values))
new_change.append(list(raw_innings_RF.values))
new_change.append(list(raw_num_DH_PA.values))

#player pos_adj var for fxn
innings_1B = new_change[0]
innings_2B = new_change[1]
innings_3B = new_change[2]
innings_SS = new_change[3]
innings_LF = new_change[4]
innings_CF = new_change[5]
innings_RF = new_change[6]
num_DH_PA = new_change[7]



def pos_adj(innings_1B=innings_1B, innings_2B=innings_2B, innings_3B=innings_3B, innings_SS=innings_SS,
            innings_LF=innings_LF, innings_CF=innings_CF, innings_RF=innings_RF, num_DH_PA=num_DH_PA):
    num_pos_adj = 0
    if innings_1B > 0:
        num_pos_adj += ((innings_1B / 9) * -12.5)
    elif innings_2B > 0:
        num_pos_adj += ((innings_2B / 9) * -12.5)
    elif innings_3B > 0:
        num_pos_adj += ((innings_3B / 9) * -12.5)
    elif innings_SS > 0:
        num_pos_adj += ((innings_SS / 9) * -12.5)
    elif innings_LF > 0:
        num_pos_adj += ((innings_LF / 9) * -12.5)
    elif innings_CF > 0:
        num_pos_adj += ((innings_CF / 9) * -12.5)
    elif innings_RF > 0:
        num_pos_adj += ((innings_RF / 9) * -12.5)
    elif num_DH_PA > 0:
        num_pos_adj += ((num_DH_PA / 4.15) / 162)
    return num_pos_adj