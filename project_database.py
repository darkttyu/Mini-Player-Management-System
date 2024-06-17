import mysql.connector

# Establishing a connection to MySQL database
# If want nyo marun yung buong program, make sure na
# adjust yung details sa pagconnect sa database and dapat may players and teams
# tables kayo
mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    password='DroU9HPwqRHnzOC',
    port='3307',
    database='player_management'
)

# Creating a cursor object to execute SQL queries
cursor = mydb.cursor()


# Function to insert a new player into the database
def insert_player(playername, age, role, winrate, recentlyused, mostused, teamparticipation, teamid):
    insert_formula = ("INSERT INTO players (playername, age, role, win_rate, recently_used, most_used, "
                      "team_participation, teamID) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)")
    player = (playername, age, role, winrate, recentlyused, mostused, teamparticipation, teamid)

    # Executing the SQL INSERT statement
    cursor.execute(insert_formula, player)

    # Committing the transaction to apply changes to the database
    mydb.commit()


# Function to retrieve player information from the database
def retrieve_player(name):
    read_formula = ("SELECT playerName, age, role, "
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
    Age: {pdata_list[1]}
    Role: {pdata_list[2]}
    Win Rate: {pdata_list[3]}%
    Recently Used: {pdata_list[4]}
    Most Used: {pdata_list[5]}
    Team Participation: {pdata_list[6]}
    Team Name: {pdata_list[7]}
    Recent Match: {pdata_list[8]}
    """
    print(player_info)


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
# - insert_playerinfo()
# - read_playerinfo()
# - update_playerinfo()
# - delete_playerinfo()
