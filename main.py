import database as pdb  # Importing the database functions from project_database module

class Statistic:
    def __init__(self, playerName=None, year=None, games_played=None,
                 most_used=None, win_rate=None, player_participation=None):

        self.__playerName = playerName
        self.__year = year
        self.__games_played = games_played
        self.__most_used = most_used
        self.__win_rate = win_rate
        self.__player_participation = player_participation

    def insert_playerstat(self):
        self.__playerName = input("Enter Player Name: ")
        self.__year = int(input("Enter Year: "))
        self.__games_played = int(input("Enter Games Played: "))
        self.__most_used = input("Enter Most Used Champion: ")
        self.__win_rate = float(input("Enter Win Rate: "))
        self.__player_participation = float(input("Enter Player Team Participation: "))

        pdb.insert_playerstat_info(self.__playerName, self.__year, self.__games_played,
                              self.__most_used, self.__win_rate, self.__player_participation)

    @staticmethod
    def retrieve_playerstat():
        print("Retrieving Player Statistic Information")

        name = input("Enter Player Name: ")
        year = int(input("Enter Year: "))

        pdb.retrieve_playerstat_info(name, year)

    @staticmethod
    def update_playerstat():
        print("Updating Player Statistic Information")

        name = input("Enter Player Name: ")
        year = int(input("Enter Year: "))
        column = input("Enter Column to be Updated: ")
        new_value = input("Enter New Value: ")
        pdb.update_playerstat_info(name, year, column, new_value)

    @staticmethod
    def delete_playerstat():
        print("Deleting Player Statistics")

        name = input("Enter Player Name: ")
        year = int(input("Enter Year: "))
        pdb.delete_player_statinfo(name, year)

class Player:
    def __init__(self, playerName=None, pFName=None, pLName=None, age=None, role_ID=None, team_ID=None):
        self.__playerName = playerName
        self.__pFName = pFName
        self.__PLName = pLName
        self.__age = age
        self.__role_ID = role_ID
        self.__team_ID = team_ID

    def insert_player(self):
        print("Inserting Player Information")

        self.__playerName = input("Enter New Player IGN: ")
        self.__pFName = input("Enter First Name: ")
        self.__PLName = input("Enter Last Name: ")
        self.__age = int(input("Age: "))
        self.__role_ID = int(input("Role ID: "))
        self.__team_ID = int(input("Team ID: "))

        pdb.insert_player(self.__playerName, self.__pFName, self.__PLName, self.__age, self.__role_ID, self.__team_ID)

    @staticmethod
    def retrieve_player():
        print("Retrieving Player Information")

        retrieve_name = input("Enter Player Name: ")
        pdb.read_player_info(retrieve_name)

    @staticmethod
    def update_player():
        print("Updating Player Information")
        IGN = input("Enter Player Name: ")
        column = input("Enter Column to be Updated: ")
        new_value = input("Enter New Value: ")

        pdb.update_player_info(IGN, column, new_value)

    @staticmethod
    def delete_player():
        print("Deleting Player Information")
        name = input("Enter Player Name:")
        pdb.delete_player_info(name)


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

    @staticmethod
    def retrieve_team():
        print("Retrieving Roster Information")
        team_ID = int(input("Enter Team ID:"))
        pdb.retrieve_roster_info(team_ID)

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

# playerstat = Statistic()
# playerstat.insert_playerstat()