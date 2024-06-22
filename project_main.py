import project_database as pdb  # Importing the database functions from project_database module

# Class definition for Player


class Player:
    def __init__(self, playername=None, age=None, role=None, teamID=None,
                 year=None, games_played=None, most_used=None,
                 win_rate=None, team_participation=None):
        # Initialize Player object with optional attributes
        self.__playername = playername
        self.__age = age
        self.__role = role
        self.__teamID = teamID
        self.__year = year
        self.__games_played = games_played
        self.__most_used = most_used
        self.__win_rate = win_rate
        self.__team_participation = team_participation

    # Method to add a new player to the database
    def new_player(self, playername, age, role):
        self.__playername = playername
        self.__age = age
        self.__role = role
        # Method to insert a new player into the database
        pdb.insert_player(self.__playername, self.__age, self.__role)

    # Method to add player statistics to the database
    def new_playerstatistics(self, playername, teamID, year, games_played, most_used, win_rate, team_participation):
        self.__playername = playername
        self.__teamID = teamID
        self.__year = year
        self.__games_played = games_played
        self.__most_used = most_used
        self.__win_rate = win_rate
        self.__team_participation = team_participation

        # Inserting player statistics into the database
        pdb.insert_playerstat(self.__playername, self.__teamID, self.__year,
                              self.__games_played, self.__most_used, self.__win_rate, self.__team_participation)

    # Static method to read player data from the database
    @staticmethod
    def read_player(playername):
        pdb.retrieve_player(playername)

    # Static method to update player data in the database
    @staticmethod
    def update_player(playername, table_column):
        pdb.update_player(playername, table_column)

    # Static method to delete player data from the database
    @staticmethod
    def delete_player(playername):
        pdb.delete_player(playername)


# Function to interactively insert a new player into the database
def insert_playerinfo():
    print("Inserting New Player to Database")

    playername = input("Enter Player Name: ")
    age = int(input("Enter Player Age: "))
    role = input("Enter Player Role: ")

    # Create Player object and insert new player data
    player = Player()
    player.new_player(playername, age, role)


# Function to interactively insert player statistics into the database
def insert_playerstats():
    print("Inserting Player Statistics to Database")

    name = input("Enter Player Name: ")
    teamID = int(input("Enter Team ID: "))
    year = int(input("Enter Year Played: "))
    games_played = int(input("Enter Number of Games Played: "))
    most_used = input("Enter Most Used Champion: ")
    win_rate = float(input("Enter Champion Win Rate: "))
    team_participation = float(input("Enter Player Team Participation: "))

    # Create Player object and insert new player statistics
    player = Player()
    player.new_playerstatistics(name, teamID, year, games_played, most_used, win_rate, team_participation)


# Function to interactively read player information from the database
def read_playerinfo():
    print("Reading Player Information From Database")
    read_playername = input("Enter Name to be Read: ")

    # Read player information from the database
    Player.read_player(read_playername)


# Function to interactively update player information in the database
def update_playerinfo():
    print("Updating Player Data in Database")

    name = input("Enter Player Name to be Updated: ")
    column = input("Enter Column to be Updated in Players Table: ")

    # Update player information in the database
    Player.update_player(name, column)


# Function to interactively delete player data from the database
def delete_playerinfo():
    print("Deleting Player Data from Database")

    name = input("Enter Player Name to be Deleted: ")

    # Delete player from the database
    Player.delete_player(name)


class Team:
    def __init__(self, team_id=None, teamName=None, recent_match=None, coach_ID=None):
        # Initialize Team object with optional attributes
        self.__team_id = team_id
        self.__teamName = teamName
        self.__recent_match = recent_match
        self.__coach_ID = coach_ID

    # Method to add a new team to the database
    def new_team(self):
        print("Inserting Team to Database")

        self.__team_id = int(input("Enter Team ID: "))
        self.__teamName = input("Enter New Team Name: ")
        self.__recent_match = input("Enter Recent Match: ")
        self.__coach_ID = int(input("Enter Coach ID: "))

        # Create Team object and insert new team data
        pdb.insert_team(self.__team_id, self.__teamName, self.__recent_match, self.__coach_ID)

    # HINDI PA TAPOS WAIT
    @staticmethod
    def retrieve_team(teamID):
        pdb.retrieve_roster(teamID)

    # Static method to update team information in the database
    @staticmethod
    def update_team():
        print("Updating Specific Team Information")

        teamID = int(input("Enter Team ID to be Updated: "))
        team_column = input("Enter Column in Team to be Updated: ")
        new_value = input("Enter New Value: ")

        pdb.update_team_info(teamID, team_column, new_value)

    # Static method to delete a team from the database
    @staticmethod
    def delete_team():
        print("Deleting Team Information")

        team_ID = int(input("Enter Team ID:"))
        pdb.delete_team_info(team_ID)

class Coach:
    def __init__(self, coach_ID=None, coachName=None, cFName=None, cLName=None):
        self.__coach_ID = coach_ID
        self.__coachName = coachName
        self.__cFName = cFName
        self.__cLName = cLName

    def new_coach(self):
        print("Inserting New Coach")
        self.__coach_ID = input("Enter Coach ID: ")
        self.__coachName = input("Enter Coach IGN: ")
        self.__cFName = input("Enter Coach First Name: ")
        self.__cLName = input("Enter Coach Last Name: ")
        pdb.insert_coach(self.__coach_ID, self.__coachName, self.__cFName, self.__cLName)

    @staticmethod
    def retrieve_coach():
        print("Reading Coach Info")

        coach_ID = int(input("Enter Coach ID: "))
        pdb.retrieve_coach_info(coach_ID)

    @staticmethod
    def update_coach():
        print("Updating Coach Information")

        coach_ID = int(input("Enter Coach ID: "))
        column = input("Enter Coach Column to be Updated: ")
        new_value = input("Enter New Value: ")
        pdb.update_coach_info(coach_ID, column, new_value)

    @staticmethod
    def delete_coach():
        print("Deleting Coach Information")

        coach_ID = int(input("Enter Coach ID to be Deleted: "))
        pdb.delete_coach_info(coach_ID)


team = Team()
team.delete_team()
