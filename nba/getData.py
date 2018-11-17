class Team:

    def __init__(self, team_name):
        self.name = team_name
        self.players = []


class Player:

    def __init__(self, gamertag):
        self.name = gamertag
        self.tip_off = Stats()
        self.regular = Stats()
        self.play_off = Stats()
        self.mid_session1 = Stats()
        self.mid_session2 = Stats()
        self.cur_pos = ""


class Stats:

    def __init__(self):
        # Season Total
        self.gp = 0
        self.pts = 0
        self.ast = 0
        self.to = 0
        self.ast_to_ratio = 0
        self.stl = 0
        self.blk = 0
        self.reb = 0
        self.oreb = 0
        self.dreb = 0
        self.fga = 0
        self.fgm = 0
        self.fg_percent = 0
        self.e_fg_percent = 0
        self.two_fga = 0
        self.two_fgm = 0
        self.two_fg_percent = 0
        self.three_fga = 0
        self.three_fgm = 0
        self.three_fg_percent = 0
        self.fta = 0
        self.ftm = 0
        self.ft_percent = 0
        self.pf_tkn = 0
        self.pf = 0
        # Per Game Stats
        self.ppg = 0
        self.apg = 0
        self.to_pg = 0
        self.ast_to_ratio_pg = 0
        self.stl_pg = 0
        self.blk_pg = 0
        self.rpg = 0
        self.oreb_pg = 0
        self.dreb_pg = 0
        self.fga_pg = 0
        self.fgm_pg = 0
        self.fg_percent_pg = 0
        self.e_fg_percent_pg = 0
        self.two_fga_pg = 0
        self.two_fgm_pg = 0
        self.two_fg_percent_pg = 0
        self.three_fga_pg = 0
        self.three_fgm_pg = 0
        self.three_fg_percent_pg = 0
        self.fta_pg = 0
        self.ftm_pg = 0
        self.ft_percent_pg = 0
        self.pf_tkn_pg = 0
        self.pf_pg = 0


