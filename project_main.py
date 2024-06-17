import project_database as pdb


class Player:
    def __init__(self, playername=None, age=None, role=None, winrate=None,
                 recentlyused=None, mostused=None, teamparticipation=None, teamid=None):
        self.playername = playername
        self.age = age
        self.role = role
        self.winrate = winrate
        self.recentlyused = recentlyused
        self.mostused = mostused
        self.teamparticipation = teamparticipation
        self.teamid = teamid

    def new_player(self):
        pdb.insert_player(self.playername, self.age, self.role, self.winrate,
                          self.recentlyused, self.mostused, self.teamparticipation, self.teamid)

    @staticmethod
    def read_player(playername):
        pdb.retrieve_player(playername)

    @staticmethod
    def update_player(playername, table_column):
        pdb.update_player(playername, table_column)

    @staticmethod
    def delete_player(playername):
        pdb.delete_player(playername)


class Team:
    def __init__(self, teamid, teamname, recent_match):
        self.teamid = teamid
        self.teamname = teamname
        self.recent_match = recent_match

    def new_team(self):
        pass

'''
def insert_playerinfo():
    print("Inserting Data to Database")

    player_name = input("Player Name: ")
    player_age = int(input("Age: "))
    player_role = input("Role: ")
    player_winrate = float(input("Winrate: "))
    player_recentlyused = input("Recently Used: ")
    player_mostused = input("Most Used: ")
    player_teamparticipation = float(input("Team Participation: "))
    player_teamid = int(input("Team ID: "))
    player = Player(player_name, player_age, player_role, player_winrate,
                    player_recentlyused, player_mostused, player_teamparticipation, player_teamid)
    player.new_player()
'''

def read_playerinfo():
    print("Reading Data From Database")
    read_playername = input("Enter Name to be Read: ")
    player = Player()
    player.read_player(read_playername)


def update_playerinfo():
    print("Updating Player Data from Database")

    name = input("Enter Player Name to be Updated: ")
    column = input("Enter Column to be Updated in Players Table: ")
    player = Player()
    player.update_player(name, column)


def delete_playerinfo():
    print("Deleting Player Data from Database")

    name = input("Enter Player Name to be Deleted: ")
    player = Player()
    player.delete_player(name)

print("Inserting Data to Database")

player_name = input("Player Name: ")
player_age = int(input("Age: "))
player_role = input("Role: ")
player_winrate = float(input("Winrate: "))
player_recentlyused = input("Recently Used: ")
player_mostused = input("Most Used: ")
player_teamparticipation = float(input("Team Participation: "))
player_teamid = int(input("Team ID: "))
player = Player(player_name, player_age, player_role, player_winrate,
                player_recentlyused, player_mostused, player_teamparticipation, player_teamid)
player.new_player()