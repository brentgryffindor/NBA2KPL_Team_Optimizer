class Team:

    def __init__(self, team_name):
        self.name = team_name
        self.players = {}

    def add_player(self, entry):
        if entry[1] in self.players:
            self.players[entry[1]].add_stats(entry)
        else:
            self.players[entry[1]] = Player(entry[1])
            self.players[entry[1]].add_stats(entry)


class Player:

    def __init__(self, gamertag):
        self.name = gamertag
        self.tip_off = None
        self.regular = None
        self.play_off = None
        self.mid_session1 = None
        self.mid_session2 = None
        self.cur_pos = ""

    def add_stats(self, entry):
        if entry[2] == 'Tip Off':
            self.tip_off = Stats(entry)
        elif entry[2] == 'Regular Season':
            self.regular = Stats(entry)
        elif entry[2] == 'Playoffs':
            self.play_off = Stats(entry)
        elif entry[2] == 'Mid-Season Tournament 1':
            self.mid_session1 = Stats(entry)
        elif entry[2] == 'Mid-Season Tournament 2':
            self.mid_session2 = Stats(entry)


class Stats:

    def __init__(self, entry):
        # Season Total
        self.gp = entry[3]                 # game played
        self.pts = entry[4]                # points
        self.ast = entry[5]                # assists
        self.to = entry[6]                 # turnovers
        self.ast_to_ratio = entry[7]       # assists / turnovers
        self.stl = entry[8]                # steals
        self.blk = entry[9]                # blocks
        self.reb = entry[10]               # rebounds
        self.oreb = entry[11]              # offensive rebounds
        self.dreb = entry[12]              # defensive rebounds
        self.fga = entry[13]               # field goal attempted
        self.fgm = entry[14]               # field goal made
        self.fg_percent = entry[15]        # field goal percentage
        self.e_fg_percent = entry[16]      # effective field goal percentage
        self.two_fga = entry[17]           # two-point field goal attempted
        self.two_fgm = entry[18]           # two-point field goal made
        self.two_fg_percent = entry[19]    # two-point field goal percentage
        self.three_fga = entry[20]         # three-point field goal attempted
        self.three_fgm = entry[21]         # three-point field goal made
        self.three_fg_percent = entry[22]  # three-point field goal percentage
        self.fta = entry[23]               # free throw attempted
        self.ftm = entry[24]               # free throw made
        self.ft_percent = entry[25]        # free throw percent
        self.pf_tkn = entry[26]            # personal fouls taken
        self.pf = entry[27]                # personal fouls
        # Per Game Stats
        self.ppg = entry[29]                    # points per game
        self.apg = entry[30]                    # assists per game
        self.to_pg = entry[31]                  # turn overs per game
        self.ast_to_ratio_pg = entry[32]        # assists / turnovers per game
        self.stl_pg = entry[33]                 # steals per game
        self.blk_pg = entry[34]                 # blocks per game
        self.rpg = entry[35]                    # rebounds per game
        self.oreb_pg = entry[36]                # offensive rebounds per game
        self.dreb_pg = entry[37]                # defensive rebounds per game
        self.fga_pg = entry[38]                 # field goal attempted per game
        self.fgm_pg = entry[39]                 # field goal made per game
        self.fg_percent_pg = entry[40]          # field goal percentage per game
        self.e_fg_percent_pg = entry[41]        # effective field goal percentage per game
        self.two_fga_pg = entry[42]             # two-point field goal attempted per game
        self.two_fgm_pg = entry[43]             # two-point field goal made per game
        self.two_fg_percent_pg = entry[43]      # two-point field goal percentage per game
        self.three_fga_pg = entry[44]           # three-point field goal attempted
        self.three_fgm_pg = entry[45]           # three-point field goal made
        self.three_fg_percent_pg = entry[46]    # three-point field goal percentage
        self.fta_pg = entry[47]                 # free throw attempted per game
        self.ftm_pg = entry[48]                 # free throw made per game
        self.ft_percent_pg = entry[49]          # free throw percentage
        self.pf_tkn_pg = entry[50]              # personal fouls taken per game
        self.pf_pg = entry[51]                  # personal fouls per game

