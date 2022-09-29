import pandas as pd

player_name_input = input('Input player full name.')

player_finder = pd.read_csv('Fill NaN for Final.csv', index_col='Name')
player_finder_rework = player_finder.infer_objects().dtypes
player_info = player_finder.loc[[player_name_input]]

teams_dict = {'COL': ['AL', 1.12], 'CIN': ['NL', 1.12], 'BOS': ['AL', 1.11], 'BAL': ['AL', 1.08], 'KCR': ['AL', 1.08],
              'TOR': ['AL', 1.06], 'ATL': ['NL', 1.05], 'CHC': ['NL', 1.03], 'ARI': ['NL', 1.03], 'MIL': ['NL', 1.02],
              'LAA': ['AL', 1.02], 'PIT': ['NL', 1.01], 'CHW': ['AL', 1.00], 'HOU': ['AL', 0.99], 'MIN': ['AL', 0.99],
              'SFG': ['NL', 0.99], 'NYY': ['AL', 0.99], 'TEX': ['AL', 0.98], 'PHI': ['NL', 0.98], 'LAD': ['NL', 0.98],
              'CLE': ['AL', 0.97], 'WSN': ['NL', 0.97], 'MIA': ['NL', 0.97], 'SDP': ['NL', 0.96], 'OAK': ['AL', 0.94],
              'DET': ['AL', 0.94], 'SEA': ['AL', 0.94], 'STL': ['NL', 0.92], 'NYM': ['NL', 0.91], 'TBR': ['AL', 0.89]}

#player bt_runs numbers
num_PA = player_info['PA']
team_raw = player_info['Team']
team_check = list(team_raw.values)
team = team_check[0]
player_wOBA = player_info['wOBA']

def bt_runs(num_PA=num_PA, team=team, player_wOBA=player_wOBA):
    lg_wOBA = 0.314
    scale_wOBA = 1.209
    lg_run_per_PA = 0.121
    nonP_AL_wRC_per_PA = 0.1225
    nonP_NL_wRC_per_PA = 0.1123
    nonP_neutral_wRC_per_PA = 0.1176
    park_factor = 1.00
    player_league = ''
    num_bt_runs = 0
    for key, values in teams_dict.items():
        if team in teams_dict.keys():
            team_key = list(teams_dict.get(team))
            player_league = team_key[0]
            park_factor = team_key[1]
    num_wRAA = ((player_wOBA - lg_wOBA) / (scale_wOBA)) * num_PA
    if player_league == 'AL':
        num_bt_runs = num_wRAA + ((lg_run_per_PA - (park_factor * lg_run_per_PA)) * num_PA) + \
                      ((lg_run_per_PA - nonP_AL_wRC_per_PA) * num_PA)
    elif player_league == 'NL':
        num_bt_runs = num_wRAA + ((lg_run_per_PA - (park_factor * lg_run_per_PA)) * num_PA) + \
                      ((lg_run_per_PA - nonP_NL_wRC_per_PA) * num_PA)
    else:
        num_bt_runs = num_wRAA + ((lg_run_per_PA - (park_factor * lg_run_per_PA)) * num_PA) + \
                      ((lg_run_per_PA - nonP_neutral_wRC_per_PA) * num_PA)
    return num_bt_runs

#player bsr_runs numbers
player_SB = player_info['SB']
player_CS = player_info['CS']
player_1B = player_info['1B']
player_BB = player_info['BB']
player_HBP = player_info['HBP']
player_IBB = player_info['IBB']
player_UBR = player_info['UBR']
player_wGDP = player_info['wGDP']

def bsr_runs(player_SB=player_SB, player_CS=player_CS, player_1B=player_1B, player_BB=player_BB, player_HBP=player_HBP,
             player_IBB=player_IBB, player_UBR=player_UBR, player_wGDP=player_wGDP):
    lg_1B = 24438
    lg_BB = 14029
    lg_HBP = 1935
    lg_IBB = 448
    lg_SB = 2345
    lg_CS = 769
    num_runSB = 0.200
    num_runCS = -0.419
    num_lg_wSB = ((lg_SB * num_runSB) + (lg_CS * num_runCS)) / (lg_1B + lg_BB + lg_HBP - lg_IBB)
    num_wSB = (player_SB * num_runSB) + (player_CS * num_runCS) - \
              (num_lg_wSB * (player_1B + player_BB + player_HBP - player_IBB))
    num_baserunning = player_UBR + num_wSB + player_wGDP
    return num_baserunning

#player fld_runs numbers
num_frm = player_info['FRM_C']
num_rSB = player_info['rSB_C']
UZR_1B = player_info['UZR_1B']
UZR_2B = player_info['UZR_2B']
UZR_3B = player_info['UZR_3B']
UZR_SS = player_info['UZR_SS']
UZR_LF = player_info['UZR_LF']
UZR_CF = player_info['UZR_CF']
UZR_RF = player_info['UZR_RF']

def fld_runs(num_frm=num_frm, num_rSB=num_rSB, UZR_1B=UZR_1B, UZR_2B=UZR_2B, UZR_3B=UZR_3B, UZR_SS=UZR_SS,
             UZR_LF=UZR_LF, UZR_CF=UZR_CF, UZR_RF=UZR_RF):
    total_UZR = 0
    num_frm = 0
    num_rSB = 0
    total_UZR = UZR_1B + UZR_2B + UZR_3B + UZR_SS + UZR_LF + UZR_CF + UZR_RF
    num_fld_runs = total_UZR + num_frm + num_rSB
    return num_fld_runs

#player pos_adj numbers
innings_1B = player_info['num_innings_1B']
innings_2B = player_info['num_innings_2B']
innings_3B = player_info['num_innings_3B']
innings_SS = player_info['num_innings_SS']
innings_LF = player_info['num_innings_LF']
innings_CF = player_info['num_innings_CF']
innings_RF = player_info['num_innings_RF']
num_DH_PA = player_info['PA_DH']

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

def lg_adj(num_PA=num_PA, team=team):
    player_league = ''
    num_lg_adj = 0
    for key, values in teams_dict.items():
        if team in teams_dict.keys():
            team_key = list(teams_dict.get(team))
            player_league = team_key[0]
    if player_league == 'AL':
        num_lg_adj += (((-1) * (-37.7 + 9.6 + 7.4 + -225.3)) / 90853) * num_PA
    elif player_league == 'NL':
        num_lg_adj += (((-1) * (-705.7 + -10.1 + -7.3 + 511.7)) / 90964) * num_PA
    else:
        num_lg_adj += .00251 * num_PA
    return num_lg_adj

def rep_lvl_runs(num_PA=num_PA):
    num_rep_lvl_runs = ((570 * (2429 / 2430)) * (9.973 / 181817)) * num_PA
    return num_rep_lvl_runs


batting_runs = bt_runs()
baserunning_runs = bsr_runs()
fielding_runs = fld_runs()
positional_adjustment = pos_adj()
league_adjustment = lg_adj()
replacement_runs = rep_lvl_runs()
runs_per_win = 9.973
def fxn_fWAR(batting_runs, baserunning_runs, fielding_runs, positional_adjustment, league_adjustment, replacement_runs, runs_per_win):
    num_fWAR = (batting_runs + baserunning_runs + fielding_runs + positional_adjustment + league_adjustment + replacement_runs) / runs_per_win
    return num_fWAR

print(fxn_fWAR())


