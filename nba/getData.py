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
        self.gp = 0                 # game played
        self.pts = 0                # points
        self.ast = 0                # assists
        self.to = 0                 # turnovers
        self.ast_to_ratio = 0       # assists / turnovers
        self.stl = 0                # steals
        self.blk = 0                # blocks
        self.reb = 0                # rebounds
        self.oreb = 0               # offensive rebounds
        self.dreb = 0               # defensive rebounds
        self.fga = 0                # field goal attempted
        self.fgm = 0                # field goal made
        self.fg_percent = 0         # field goal percentage
        self.e_fg_percent = 0       # effective field goal percentage
        self.two_fga = 0            # two-point field goal attempted
        self.two_fgm = 0            # two-point field goal made
        self.two_fg_percent = 0     # two-point field goal percentage
        self.three_fga = 0          # three-point field goal attempted
        self.three_fgm = 0          # three-point field goal made
        self.three_fg_percent = 0   # three-point field goal percentage
        self.fta = 0                # free throw attempted
        self.ftm = 0                # free throw made
        self.ft_percent = 0         # free throw percent
        self.pf_tkn = 0             # personal fouls taken
        self.pf = 0                 # personal fouls
        # Per Game Stats
        self.ppg = 0                    # points per game
        self.apg = 0                    # assists per game
        self.to_pg = 0                  # turn overs per game
        self.ast_to_ratio_pg = 0        # assists / turnovers per game
        self.stl_pg = 0                 # steals per game
        self.blk_pg = 0                 # blocks per game
        self.rpg = 0                    # rebounds per game
        self.oreb_pg = 0                # offensive rebounds per game
        self.dreb_pg = 0                # defensive rebounds per game
        self.fga_pg = 0                 # field goal attempted per game
        self.fgm_pg = 0                 # field goal made per game
        self.fg_percent_pg = 0          # field goal percentage per game
        self.e_fg_percent_pg = 0        # effective field goal percentage per game
        self.two_fga_pg = 0             # two-point field goal attempted per game
        self.two_fgm_pg = 0             # two-point field goal made per game
        self.two_fg_percent_pg = 0      # two-point field goal percentage per game
        self.three_fga_pg = 0           # three-point field goal attempted
        self.three_fgm_pg = 0           # three-point field goal made
        self.three_fg_percent_pg = 0    # three-point field goal percentage
        self.fta_pg = 0                 # free throw attempted per game
        self.ftm_pg = 0                 # free throw made per game
        self.ft_percent_pg = 0          # free throw percentage
        self.pf_tkn_pg = 0              # personal fouls taken per game
        self.pf_pg = 0                  # personal fouls per game

