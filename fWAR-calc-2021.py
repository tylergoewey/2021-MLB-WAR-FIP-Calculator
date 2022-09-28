import pandas as pd

player_read = pd.read_csv('Project Pull For Sort.csv')
player_name_input = input('Input player full name.')

player = {}

teams_dict = {COL: [AL, 112], CIN: [NL, 112], BOS: [AL, 111], BAL: [AL, 108], KCR: [AL, 108], TOR: [AL, 106], ATL: [NL, 105],
              CHC: [NL, 103], ARI: [NL, 103], MIL: [NL, 102], LAA: [AL, 102], PIT: [NL, 101], CHW: [AL, 100], HOU: [AL, 99],
              MIN: [AL, 99], SFG: [NL, 99], NYY: [AL, 99], TEX: [AL, 98], PHI: [NL, 98], LAD: [NL, 98], CLE: [AL, 97], WSN: [NL, 97],
              MIA: [NL, 97], SDP: [NL, 96], OAK: [AL, 94], DET: [AL, 94], SEA: [AL, 94], STL: [NL, 92], NYM: [NL, 91], TBR: [AL, 89]}
def fxn_player_name(player_name_input):
    for name in range(len(player_read.Name)):
        if player_name_input == player_read.Name[name]:
            return True
        else:
            return False

if fxn_player_name(player_name_input) == True:
    player.update(dict(new_csv_total.loc[0].items()))

def bt_runs():
    lg_wOBA = 0.314
    scale_wOBA = 1.209
    lg_run_per_PA = 0.121
    nonP_AL_wRC_per_PA = 0.1225
    nonP_NL_wRC_per_PA = 0.1123
    nonP_neutral_wRC_per_PA = 0.1176
    park_factor = 100
    num_PA =
    num_wRAA = ((player_wOBA - lg_wOBA) / (scale_wOBA)) * num_PA
    if player in lg_AL:
        return num_bt_runs = num_wRAA + (lg_run_per_PA - ((park_factor * lg_run_per_PA) * num_PA)) + ((lg_run_per_PA - nonP_AL_wRC_per_PA) * num_PA)
    elif player in lg_NL:
        return num_bt_runs = num_wRAA + (lg_run_per_PA - ((park_factor * lg_run_per_PA) * num_PA)) + ((lg_run_per_PA - nonP_NL_wRC_per_PA) * num_PA)
    else:
        return num_bt_runs = num_wRAA + (lg_run_per_PA - ((park_factor * lg_run_per_PA) * num_PA)) + ((lg_run_per_PA - nonP_neutral_wRC_per_PA) * num_PA)
    return

def bsr_runs():
    lg_1B = 24438
    lg_BB = 14029
    lg_HBP = 1935
    lg_IBB = 448
    lg_SB = 2345
    lg_CS = 769
    num_runSB = 0.200
    num_runCS = -0.419
    num_lg_wSB = ((lg_SB * lg_runSB) + (lg_CS * lg_runCS)) / (lg_1B + lg_BB + lg_HBP - lg_IBB)
    num_wSB = (player_SB * num_runSB) + (player_CS * num_runCS) - (num_lg_wSB * (player_1B + player_BB + player_HBP - player_IBB))
    num_baserunning = player_UBR + num_wSB + player_wGDP
    return num_baserunning

def fld_runs():
    total_UZR = 0
    num_frm =
    num_rSB =
    for UZR in key:
        total_UZR += value
    num_fld_runs = total_UZR + num_frm + num_rSB
    return num_fld_runs

def pos_adj():
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

def lg_adj():
    num_lg_adj = 0
    if player in lg_AL:
        num_lg_adj += (((-1) * (-37.7 + 9.6 + 7.4 + -225.3)) / 90853) * num_PA
    elif player in lg_NL:
        num_lg_adj += (((-1) * (-705.7 + -10.1 + -7.3 + 511.7)) / 90964) * num_PA
    else:
        num_lg_adj += .00251 * num_PA
    return num_lg_adj

def rep_lvl_runs():
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


