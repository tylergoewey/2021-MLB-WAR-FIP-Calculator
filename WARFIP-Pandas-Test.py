import pandas as pd
import numpy as np


bat = pd.read_csv('Project Batting pull.csv')
_c = pd.read_csv('Catcher innings.csv')
_1b = pd.read_csv('1B innings.csv')
_2b = pd.read_csv('2B innings.csv')
_3b = pd.read_csv('3B innings.csv')
_ss = pd.read_csv('SS innings.csv')
_lf = pd.read_csv('LF innings.csv')
_cf = pd.read_csv('CF innings.csv')
_rf = pd.read_csv('RF innings.csv')
_dh = pd.read_csv('Splits Leaderboard Data as DH.csv')
_playerID = pd.read_csv('All Player IDS and Names.csv')

new_csv_c = pd.merge(bat, _c, on='playerid', how='outer')
new_csv_1b = pd.merge(new_csv_c, _1b, on='playerid', how='outer')
new_csv_2b = pd.merge(new_csv_1b, _2b, on='playerid', how='outer')
new_csv_3b = pd.merge(new_csv_2b, _3b, on='playerid', how='outer')
new_csv_ss = pd.merge(new_csv_3b, _ss, on='playerid', how='outer')
new_csv_lf = pd.merge(new_csv_ss, _lf, on='playerid', how='outer')
new_csv_cf = pd.merge(new_csv_lf, _cf, on='playerid', how='outer')
new_csv_rf = pd.merge(new_csv_cf, _rf, on='playerid', how='outer')
new_csv_dh = pd.merge(new_csv_rf, _dh, on='playerid', how='outer')
new_csv_total = pd.merge(new_csv_dh, _playerID, on='playerid', how='outer')

new_csv_total.to_csv('Project Pull For Sort.csv')
final_read_csv = pd.read_csv('Project Pull For Sort.csv')

player_name_input = input('Input player full name.')


def fxn_player_name(player_name_input):
    player = {}
    for name in range(len(new_csv_total.Name)):
        if player_name_input == new_csv_total.Name[name]:
            df = pd.DataFrame(final_read_csv)
            player_name_index = df[df['Name'] == player_name_input].index.values
            player.update(dict(new_csv_total.loc[player_name_index].items()))
    return player

player_dictionary = fxn_player_name(player_name_input)
print(player_dictionary.values())

