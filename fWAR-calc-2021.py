class FangraphsWAR:

    def __init__(self):
        self.batting_runs = batting_runs
        self.baserunning_runs = baserunning_runs
        self.fielding_runs = fielding_runs
        self.positional_adjustment = positional_adjustment
        self.league_adjustment = league_adjustment
        self.replacement_runs = replacement_runs
        self.runs_per_win = runs_per_win
        num_fWAR = (
                               self.batting_runs + self.baserunning_runs + self.fielding_runs + self.positional_adjustment + self.league_adjustment + self.replacement_runs) / (
                       self)

    def bt_runs(self):
        lg_wOBA = 0.314
        scale_wOBA = 1.209
        lg_run_per_PA = 0.121
        nonP_AL_wRC_per_PA = 0.1225
        nonP_NL_wRC_per_PA = 0.1123
        nonP_neutral_wRC_per_PA = 0.1176
        park_factor =
        num_PA =
        num_wRAA = ((player_wOBA - lg_wOBA) / (scale_wOBA)) * num_PA
        if player in lg_AL:
            return num_bt_runs = num_wRAA + (lg_run_per_PA - ((park_factor * lg_run_per_PA) * num_PA)) + (
                        (lg_run_per_PA - nonP_AL_wRC_per_PA) * num_PA)
        elif player in lg_NL:
            return num_bt_runs = num_wRAA + (lg_run_per_PA - ((park_factor * lg_run_per_PA) * num_PA)) + (
                        (lg_run_per_PA - nonP_NL_wRC_per_PA) * num_PA)
        else:
            return num_bt_runs = num_wRAA + (lg_run_per_PA - ((park_factor * lg_run_per_PA) * num_PA)) + (
                        (lg_run_per_PA - nonP_neutral_wRC_per_PA) * num_PA)
        return

    def bsr_runs(self):
        lg_1B = 24438
        lg_BB = 14029
        lg_HBP = 1935
        lg_IBB = 448
        lg_SB = 2345
        lg_CS = 769
        num_runSB = 0.200
        num_runCS = -0.419
        num_lg_wSB = ((lg_SB * lg_runSB) + (lg_CS * lg_runCS)) / (lg_1B + lg_BB + lg_HBP - lg_IBB)
        num_wSB = (player_SB * num_runSB) + (player_CS * num_runCS) - (
                    num_lg_wSB * (player_1B + player_BB + player_HBP - player_IBB))
        num_baserunning = player_UBR + num_wSB + player_wGDP
        return num_baserunning

    def fld_runs(self):
        total_UZR = 0
        num_frm =
        num_rSB =
        for UZR in key:
            total_UZR += value
        num_fld_runs = total_UZR + num_frm + num_rSB
        return num_fld_runs

    def pos_adj(self):
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

    def lg_adj(self):
        num_lg_adj = 0
        if player in lg_AL:
            num_lg_adj += (((-1) * (-37.7 + 9.6 + 7.4 + -225.3)) / 90853) * num_PA
        elif player in lg_NL:
            num_lg_adj += (((-1) * (-705.7 + -10.1 + -7.3 + 511.7)) / 90964) * num_PA
        else:
            num_lg_adj += .00251 * num_PA
        return num_lg_adj

    def rep_lvl_runs(self):
        num_rep_lvl_runs = ((570 * (2429 / 2430)) * (9.973 / 181817)) * num_PA
        return num_rep_lvl_runs

    runs_per_win = 9.973