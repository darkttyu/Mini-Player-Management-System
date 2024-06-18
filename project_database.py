import mysql.connector

# Establishing a connection to MySQL database
# Make sure to adjust these details to match your MySQL server configuration
mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    password='DroU9HPwqRHnzOC',
    port='3307',  # Adjust the port number as per your MySQL server configuration
    database='player_management'  # Ensure this database exists in your MySQL server
)

# Creating a cursor object to execute SQL queries
cursor = mydb.cursor()


# Function to insert a new player into the database
def insert_player(playername, age, role, winrate, games_played, recentlyused, mostused, teamparticipation, teamid):
    # Checks if a player already exists in the database
    check_formula = ("SELECT playerName FROM players WHERE playerName = %s")
    cursor.execute(check_formula, (playername,))
    result = cursor.fetchone()

    if result is None:
        insert_formula = ("INSERT INTO players (playerName, age, role, games_played, win_rate, recently_used, most_used, "
                          "team_participation, teamID) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)")
        player = (playername, age, role, winrate, games_played, recentlyused, mostused, teamparticipation, teamid)

        # Executing the SQL INSERT statement
        cursor.execute(insert_formula, player)

        # Committing the transaction to apply changes to the database
        mydb.commit()
    else:
        print("Cannot Insert Player. Player already exists.")

# Function to insert a new team into the database
def insert_team(team_id, team_name, recent_match):
    check_team = ("SELECT teamName FROM teams WHERE teamName = %s")
    cursor.execute(check_team, (team_name,))
    result = cursor.fetchone()

    if result is None:
        insert_formula = ("INSERT INTO teams (teamID, teamName, recent_match) VALUES (%s, %s, %s)")
        team = (team_id, team_name, recent_match)

        cursor.execute(insert_formula, team)
        mydb.commit()
    else:
        print("Cannot Insert Team. Team already exists.")

# Function to retrieve player information from the database
def retrieve_player(name):
    read_formula = ("SELECT playerName, age, role, games_played, "
                    "win_rate, recently_used, most_used, "
                    "team_participation, teamName, recent_match "
                    "FROM PLAYERS INNER JOIN "
                    "TEAMS ON PLAYERS.TEAMID = TEAMS.TEAMID "
                    "WHERE playername = %s")

    # Executing the SQL SELECT statement
    cursor.execute(read_formula, (name,))

    # Fetching the first row of the result
    player_data = cursor.fetchone()
    pdata_list = list(player_data)

    # Printing retrieved player information
    print("\nRetrieved Data from Database")
    player_info = f"""
    Player Name: {pdata_list[0]}
    Team Name: {pdata_list[8]}
    Age: {pdata_list[1]}
    Role: {pdata_list[2]}
    Total Games Played: {pdata_list[3]}
    Win Rate: {pdata_list[4]}%
    Recently Used: {pdata_list[5]}
    Most Used: {pdata_list[6]}
    Team Participation: {pdata_list[7]}
    Recent Match: {pdata_list[9]}
    """
    print(player_info)

# Function to retrieve roster of players in a team from the database
def retrieve_roster(teamID):
    retrieve_formula = ("SELECT playerName, age, role, games_played, win_rate, " 
                        "recently_used, most_used, team_participation FROM PLAYERS "
                        "WHERE teamID = %s")
    cursor.execute(retrieve_formula, (teamID, ))
    roster_data = cursor.fetchall()
    roster_list = [list(player) for player in roster_data]

    retrieve_team_formula = ("SELECT teamName, recent_match FROM teams WHERE teamID = %s")
    cursor.execute(retrieve_team_formula, (teamID,))
    singleteam_info = cursor.fetchall()
    convertedteam_info = [list(team) for team in singleteam_info]

    team_info = f"""Team Name: {convertedteam_info[0][0]}
Recent Match: {convertedteam_info[0][1]}"""
    print(team_info)

    for x in range(5):
        roster_info = f"""
    [{x+1}] Player Name: {roster_list[x][0]}
    Age: {roster_list[x][1]}
    Role: {roster_list[x][2]}
    Total Games Played: {roster_list[x][3]}
    Win Rate: {roster_list[x][4]}
    Recently Used: {roster_list[x][5]}
    Most Used: {roster_list[x][6]}
    Team Participation: {roster_list[x][7]}
    """

        print(roster_info)

# Function to update player information in the database
def update_player(name, column):
    column_list = ['playerName', 'age', 'role', 'win_rate', 'recent_used', 'most_used', 'team_participation']

    # Checking if the specified column is valid
    if column not in column_list:
        print("Invalid Column")
        return

    # Handling different data types for update
    elif column == 'win_rate' or column == 'team_participation':
        new_value = float(input("Enter New Value: "))
    elif column == 'age':
        new_value = int(input("Enter new Value: "))
    else:
        new_value = input("Enter New Value: ")

    # Constructing the SQL UPDATE statement
    update_formula = ("UPDATE PLAYERS "
                      "SET " + column + " = %s "
                                        "WHERE playerName = %s")

    # Executing the SQL UPDATE statement
    cursor.execute(update_formula, (new_value, name))
    print("Table Updated Successfully!")

    # Committing the transaction to apply changes to the database
    mydb.commit()

# Function to delete a player from the database
def delete_player(name):
    delete_formula = ("DELETE FROM PLAYERS WHERE playerName = %s")

    # Executing the SQL DELETE statement
    cursor.execute(delete_formula, (name,))
    print("Player Deleted Successfully!")

    # Committing the transaction to apply changes to the database
    mydb.commit()

# The following code shows how to use the above functions to interact with the database:
# - insert_player()
# - retrieve_player()
# - update_player()
# - delete_player()
