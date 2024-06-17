import project_database as pdb  # Importing the database functions from project_database module


class Player:
    def __init__(self, playername=None, age=None, role=None, winrate=None,
                 recentlyused=None, mostused=None, teamparticipation=None, teamid=None):
        # Initialize Player object with optional attributes
        self.playername = playername
        self.age = age
        self.role = role
        self.winrate = winrate
        self.recentlyused = recentlyused
        self.mostused = mostused
        self.teamparticipation = teamparticipation
        self.teamid = teamid

    def new_player(self):
        # Method to insert a new player into the database
        pdb.insert_player(self.playername, self.age, self.role, self.winrate,
                          self.recentlyused, self.mostused, self.teamparticipation, self.teamid)

    @staticmethod
    def read_player(playername):
        # Static method to retrieve player information from the database
        pdb.retrieve_player(playername)

    @staticmethod
    def update_player(playername, table_column):
        # Static method to update player information in the database
        pdb.update_player(playername, table_column)

    @staticmethod
    def delete_player(playername):
        # Static method to delete a player from the database
        pdb.delete_player(playername)


class Team:
    def __init__(self, teamid, teamname, recent_match):
        # Initialize Team object with attributes
        self.teamid = teamid
        self.teamname = teamname
        self.recent_match = recent_match

    def new_team(self):
        # Method to handle creating a new team (currently not implemented)
        pass


def insert_playerinfo():
    # Function to interactively insert player data into the database
    print("Inserting Data to Database")

    player_name = input("Player Name: ")
    player_age = int(input("Age: "))
    player_role = input("Role: ")
    player_winrate = float(input("Winrate: "))
    player_recentlyused = input("Recently Used: ")
    player_mostused = input("Most Used: ")
    player_teamparticipation = float(input("Team Participation: "))
    player_teamid = int(input("Team ID: "))

    # Create Player object and insert data into the database
    player = Player(player_name, player_age, player_role, player_winrate,
                    player_recentlyused, player_mostused, player_teamparticipation, player_teamid)
    player.new_player()


def read_playerinfo():
    # Function to interactively read player data from the database
    print("Reading Data From Database")
    read_playername = input("Enter Name to be Read: ")

    # Read player information from the database
    player = Player()
    player.read_player(read_playername)


def update_playerinfo():
    # Function to interactively update player data in the database
    print("Updating Player Data from Database")

    name = input("Enter Player Name to be Updated: ")
    column = input("Enter Column to be Updated in Players Table: ")

    # Update player information in the database
    player = Player()
    player.update_player(name, column)


def delete_playerinfo():
    # Function to interactively delete player data from the database
    print("Deleting Player Data from Database")

    name = input("Enter Player Name to be Deleted: ")

    # Delete player from the database
    player = Player()
    player.delete_player(name)

# The following code shows how to use the above functions to interact with the database:
# - insert_playerinfo()
# - read_playerinfo()
# - update_playerinfo()
# - delete_playerinfo()


