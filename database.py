import mysql.connector
from mysql.connector import errorcode

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

# Function to check admin credentials in the admin table
def check_admin(username, password):
    # SQL query to select admin credentials
    login_formula = ("SELECT * FROM admin WHERE admin_user = %s AND password = %s")
    # Execute the query with the provided username and password
    cursor.execute(login_formula, (username, password))
    # Fetch one result
    retrieve_admin = cursor.fetchone()

    # If no result is found, return False
    if retrieve_admin is None:
        return False
    # If a result is found, return True
    else:
        return True

# Function to insert player performance statistics
def insert_playerstat_info(name, year, games, most_used, wr, participation):
    # Check if the player exists in the PLAYER table
    check_player = ("SELECT playerName FROM PLAYER where playerName = %s")
    cursor.execute(check_player, (name,))
    result = cursor.fetchone()

    # If the player does not exist, return 'PLDNE' (Player Does Not Exist)
    if result is None:
        return 'PLDNE'

    # Check if the player statistics already exist for the given year
    check_formula = ("SELECT playerName, year_played FROM PLAYER_PERFORMANCE WHERE playerName = %s AND year_played = %s")
    cursor.execute(check_formula, (name, year))
    result = cursor.fetchone()

    # If the statistics do not exist, insert the new record
    if result is None:
        insert_formula = ("INSERT INTO PLAYER_PERFORMANCE (playerName, year_played, games_played, "
                          "most_used, win_rate, player_participation) "
                          "VALUES (%s, %s, %s, %s, %s, %s)")
        cursor.execute(insert_formula, (name, year, games, most_used, wr, participation))
        mydb.commit()  # Commit the transaction
        return 'PSIS'  # Player Statistics Inserted Successfully
    # If the statistics already exist, return 'PSAE' (Player Statistics Already Exist)
    else:
        return 'PSAE'

# Function to retrieve player performance statistics
def retrieve_playerstat_info(name, year):
    retrieve_player_formula = "SELECT * FROM player_performance WHERE playerName = %s"
    cursor.execute(retrieve_player_formula, (name,))

    # Fetch one result
    retrieved_player = cursor.fetchone()

    # If no result is found, return 'PDNE' (Player Statistics Do Not Exist)
    if retrieved_player is None:
        return 'PDNE'

    # Ensure all results from the previous query are read
    cursor.fetchall()  # Fetch all remaining results (if any) and discard them

    retrieve_stat_formula = "SELECT * FROM player_performance WHERE playerName = %s AND year_played = %s"
    cursor.execute(retrieve_stat_formula, (name, year))
    retrieved_stat = cursor.fetchone()

    if retrieved_stat is not None:
        return list(retrieved_stat)
    else:
        return 'PSDNE'


# Function to update player performance statistics
def update_playerstat_info(name, year, column, new_value):
    player_stat_list = ['year_played', 'games_played', 'most_used', 'win_rate', 'player_participation']

    # Check if the specified column is valid
    if column not in player_stat_list:
        return False

    # Check if the player exists
    check_player_formula = "SELECT * FROM PLAYER WHERE playerName = %s"
    cursor.execute(check_player_formula, (name,))
    player_info = cursor.fetchone()

    # If the player does not exist, return 'PDNE' (Player Does Not Exist)
    if player_info is None:
        return 'PDNE'

    cursor.fetchall()

    # Check if the player statistics exist for the given year
    retrieve_stat_formula = "SELECT * FROM player_performance WHERE playerName = %s AND year_played = %s"
    cursor.execute(retrieve_stat_formula, (name, year))
    retrieved_stat = cursor.fetchone()

    # If the statistics do not exist, return 'PSDNE' (Player Statistics Do Not Exist)
    if retrieved_stat is None:
        return 'PSDNE'

    # Check if the new year already exists for the player

    if column == 'year_played':
        check_year = "SELECT year_played FROM PLAYER_PERFORMANCE WHERE playerName = %s AND year_played = %s"
        cursor.execute(check_year, (name, new_value))
        result = cursor.fetchone()
        print(result)

        if result is not None:
            return 'PSYAE'

    # Update player statistics
    update_playerstat_formula = ("UPDATE PLAYER_PERFORMANCE SET " + column +
                                        " = %s WHERE playerName = %s AND year_played = %s")
    cursor.execute(update_playerstat_formula, (new_value, name, year))
    mydb.commit()  # Commit the transaction
    return 'PSUS'  # Player Statistics Updated Successfull


# Function to delete player performance statistics
def delete_player_statinfo(name, year):
    check_player = "SELECT playerName FROM PLAYER WHERE playerName = %s"
    cursor.execute(check_player, (name,))
    result = cursor.fetchone()
    if result is None:
        return 'PDNE'

    # Ensure all results are read
    cursor.fetchall()  # This ensures that any remaining results are read and the cursor is ready for the next query

    # Check if the player statistics for the specific year exist
    check_stat = "SELECT playerName, year_played FROM player_performance WHERE playerName = %s AND year_played = %s"
    cursor.execute(check_stat, (name, year))
    result = cursor.fetchone()
    if result is None:
        return 'PSTDNE'

    # Ensure all results are read
    cursor.fetchall()  # This ensures that any remaining results are read and the cursor is ready for the next query

    # Delete the player statistics
    delete_player_formula = "DELETE FROM player_performance WHERE playerName = %s AND year_played = %s"
    cursor.execute(delete_player_formula, (name, year))
    mydb.commit()  # Commit the transaction
    return True  # Deletion was successful

# Function to insert a new player into the PLAYER table
def insert_player(IGN, FName, LName, age, role_ID, team_ID):
    # Checks if the player already exists in the database
    check_IGN_formula = ("SELECT playerName FROM PLAYER WHERE playerName = %s")
    cursor.execute(check_IGN_formula, (IGN,))
    IGN_result = cursor.fetchone()

    # Check the number of players in the specified team
    check_teamCount_formula = ("SELECT COUNT(team_ID) FROM PLAYER WHERE team_ID = %s")
    cursor.execute(check_teamCount_formula, (team_ID,))
    count_result = cursor.fetchone()

    check_team = ("SELECT team_ID FROM TEAM WHERE team_ID = %s")
    cursor.execute(check_team, (team_ID,))
    result = cursor.fetchone()

    if result is None:
        return 'TDNE'

    # If the team has 5 or fewer players
    if count_result[0] <= 5:
        # If the player does not exist, insert the new player
        if IGN_result is None:
            insert_formula = ("INSERT INTO PLAYER (playerName, pFName, PLName, age, role_ID, team_ID"
                              ") VALUES (%s, %s, %s, %s, %s, %s)")
            player = (IGN, FName, LName, age, role_ID, team_ID)

            # Execute the SQL INSERT statement
            cursor.execute(insert_formula, player)
            # Commit the transaction to apply changes to the database
            mydb.commit()
            return True
        else:
            return 'PLAE'  # Player Already Exists
    else:
        return 'MAX'  # Maximum number of players in the team reached

# Function to read player information from the database
def read_player_info(IGN):
    # Check if the player exists in the database
    check_IGN_formula = ("SELECT playerName FROM PLAYER WHERE playerName = %s")
    cursor.execute(check_IGN_formula, (IGN,))
    result = cursor.fetchone()

    # If the player does not exist, return 'PLDNE' (Player Does Not Exist)
    if result is None:
        return 'PLDNE'
    else:
        # Retrieve player information along with role, team, and coach details
        retrieve_player_formula = ("SELECT p.playerName, p.pFName, p.pLName, p.age, "
                                   "r.roleName, t.teamName, c.coachName "
                                   "FROM player AS p "
                                   "JOIN role AS r ON p.role_ID = r.role_ID "
                                   "JOIN team AS t ON p.team_ID = t.team_ID "
                                   "JOIN coach AS c ON t.coach_ID = c.coach_ID "
                                   "WHERE p.playerName = %s")
        cursor.execute(retrieve_player_formula, (IGN,))
        retrieved_info = cursor.fetchone()
        return retrieved_info

# Function to update player information
def update_player_info(IGN, column, new_value):
    # List of valid columns for updating
    column_list = ['playerName', 'pFName', 'pLName', 'age', 'role_ID', 'team_ID']

    # Check if the specified column is valid
    if column not in column_list:
        return 'CDNE'  # Column Does Not Exist

    # Check if the player exists in the database
    check_player = "SELECT playerName FROM PLAYER WHERE playerName = %s"
    cursor.execute(check_player, (IGN,))
    result = cursor.fetchone()

    # If the player does not exist, return 'PDNE' (Player Does Not Exist)
    if result is None:
        return 'PDNE'

    # Update the player name and associated performance records
    if column == 'playerName':
        update_player = ("UPDATE PLAYER SET playerName = %s WHERE playerName = %s")
        update_player_stat = ("UPDATE PLAYER_PERFORMANCE SET playerName = %s WHERE playerName = %s")
        cursor.execute(update_player, (new_value, IGN,))
        cursor.execute(update_player_stat, (new_value, IGN))
        mydb.commit()
        return 'PNUS'  # Player Name Updated Successfully

    # Update the team ID after checking for constraints
    elif column == 'team_ID':
        checkteam_ID = ("SELECT team_ID FROM TEAM WHERE team_ID = %s")
        cursor.execute(checkteam_ID, (new_value,))
        result = cursor.fetchone()

        # If the team does not exist, return 'TDNE' (Team Does Not Exist)
        if result is None:
            return 'TDNE'

        # Check the number of players in the new team
        check_teamcount = ("SELECT COUNT(*) FROM PLAYER WHERE team_ID = %s")
        cursor.execute(check_teamcount, (new_value,))
        result = cursor.fetchone()

        # If the new team already has the maximum number of players, return 'MAX'
        if result[0] >= 6:
            return 'MAX'
        else:
            update_teamID = ("UPDATE PLAYER SET team_ID = %s WHERE playerName = %s")
            cursor.execute(update_teamID, (new_value, IGN))
            mydb.commit()
            return 'PTIDUS'  # Player Team ID Updated Successfully

    # Update other player information
    else:
        update_player = ("UPDATE PLAYER SET " + column + " = %s WHERE playerName = %s")
        cursor.execute(update_player, (new_value, IGN))
        mydb.commit()
        return 'PIUS'  # Player Information Updated Successfully

# Function to delete player information from the database
def delete_player_info(name):
    # Check if the player exists in the database
    check_player = ("SELECT playerName FROM PLAYER WHERE playerName = %s")
    cursor.execute(check_player, (name,))
    result = cursor.fetchone()

    # If the player does not exist, return 'PDNE' (Player Does Not Exist)
    if result is None:
        return 'PDNE'
    else:
        # Delete the player from the database
        delete_player_formula = ("DELETE FROM PLAYER WHERE playerName = %s")
        cursor.execute(delete_player_formula, (name,))
        mydb.commit()
        return True  # Player deleted successfully

# Function to inert a new team into the TEAM table
def insert_team(team_id, team_name, recent_match, coach_ID):

    try:
        # Query to check if Team ID Exists
        check_teamID = ("SELECT team_ID FROM TEAM WHERE team_ID = %s")
        cursor.execute(check_teamID, (team_id,))
        result = cursor.fetchone()

        if result is not None:
            return 'TIDAE' # Team ID already exists

        # Checks if a team already exists in the database
        check_team = ("SELECT teamName FROM TEAM WHERE teamName = %s")
        cursor.execute(check_team, (team_name,))
        result = cursor.fetchone()

        if result is not None:
            return 'TNAE' # Team Name already exists

        # Checks if a team already handles a team
        check_coach = ("SELECT coach_ID FROM TEAM WHERE coach_ID = %s")
        cursor.execute(check_coach, (coach_ID,))
        result = cursor.fetchone()

        if result is not None:
            return 'CAT' # Coach already taken

        # Team Insertion
        insert_formula = ("INSERT INTO TEAM (team_ID, teamName, recent_match, coach_ID) VALUES (%s, %s, %s, %s)")
        team = (team_id, team_name, recent_match, coach_ID)

        # Executing the SQL INSERT statement
        cursor.execute(insert_formula, team)

        # Committing the transaction to apply changes to the database
        mydb.commit()
        return 'TIS'

    except mysql.connector.IntegrityError as e:
        if e.errno == errorcode.ER_DUP_ENTRY:
            return 'TIDAE' # Team ID already exists

def retrieve_roster_info(teamID):
    # Coach and Team Retrieval
    retrieve_coach_team_formula = ("SELECT t.teamName, c.coachName "
                                   "FROM team AS t "
                                   "JOIN coach as c ON t.coach_ID = c.coach_ID "
                                   "WHERE t.team_ID = %s")
    cursor.execute(retrieve_coach_team_formula, (teamID,))
    team_coach_info = cursor.fetchone()

    if team_coach_info is None:
        return False, False  # Return False values if no coach or team found

    team_coach_info = list(team_coach_info)

    # Check if any players exist in the team
    check_teamID_formula = "SELECT * FROM PLAYER WHERE team_ID = %s"
    cursor.execute(check_teamID_formula, (teamID,))
    result = cursor.fetchall()

    if not result:
        return False, False  # Return False values if no players found

    # Roster Retrieval
    retrieve_roster_formula = ("SELECT p.playerName, p.pFName, p.pLName, p.age, r.roleName "
                               "FROM player AS p "
                               "JOIN role AS r ON p.role_ID = r.role_ID "
                               "WHERE p.team_ID = %s")
    cursor.execute(retrieve_roster_formula, (teamID,))
    roster_list = cursor.fetchall()

    return team_coach_info, roster_list


# Sorting
def rteam_AgeASC(teamID):
    # Coach and Team Retrieval
    retrieve_coach_team_formula = ("SELECT t.teamName, c.coachName "
                                   "FROM team AS t "
                                   "JOIN coach as c ON t.coach_ID = c.coach_ID "
                                   "WHERE t.team_ID = %s")
    cursor.execute(retrieve_coach_team_formula, (teamID,))
    team_coach_info = cursor.fetchone()

    if team_coach_info is None:
        return False, False  # Return False values if no coach or team found

    team_coach_info = list(team_coach_info)

    # Check if any players exist in the team
    check_teamID_formula = "SELECT * FROM PLAYER WHERE team_ID = %s"
    cursor.execute(check_teamID_formula, (teamID,))
    result = cursor.fetchall()

    if not result:
        return False, False  # Return False values if no players found

    # Roster Retrieval
    retrieve_roster_formula = ("SELECT p.playerName, p.pFName, p.pLName, p.age, r.roleName "
                               "FROM player AS p "
                               "JOIN role AS r ON p.role_ID = r.role_ID "
                               "WHERE p.team_ID = %s"
                               "ORDER BY AGE ASC")
    cursor.execute(retrieve_roster_formula, (teamID,))
    roster_list = cursor.fetchall()

    return team_coach_info, roster_list

def rteam_AgeDESC(teamID):
    # Coach and Team Retrieval
    retrieve_coach_team_formula = ("SELECT t.teamName, c.coachName "
                                   "FROM team AS t "
                                   "JOIN coach as c ON t.coach_ID = c.coach_ID "
                                   "WHERE t.team_ID = %s")
    cursor.execute(retrieve_coach_team_formula, (teamID,))
    team_coach_info = cursor.fetchone()

    if team_coach_info is None:
        return False, False  # Return False values if no coach or team found

    team_coach_info = list(team_coach_info)

    # Check if any players exist in the team
    check_teamID_formula = "SELECT * FROM PLAYER WHERE team_ID = %s"
    cursor.execute(check_teamID_formula, (teamID,))
    result = cursor.fetchall()

    if not result:
        return False, False  # Return False values if no players found

    # Roster Retrieval
    retrieve_roster_formula = ("SELECT p.playerName, p.pFName, p.pLName, p.age, r.roleName "
                               "FROM player AS p "
                               "JOIN role AS r ON p.role_ID = r.role_ID "
                               "WHERE p.team_ID = %s"
                               "ORDER BY AGE DESC")
    cursor.execute(retrieve_roster_formula, (teamID,))
    roster_list = cursor.fetchall()

    return team_coach_info, roster_list

def rteampName_ASC(teamID):
    # Coach and Team Retrieval
    retrieve_coach_team_formula = ("SELECT t.teamName, c.coachName "
                                   "FROM team AS t "
                                   "JOIN coach as c ON t.coach_ID = c.coach_ID "
                                   "WHERE t.team_ID = %s")
    cursor.execute(retrieve_coach_team_formula, (teamID,))
    team_coach_info = cursor.fetchone()

    if team_coach_info is None:
        return False, False  # Return False values if no coach or team found

    team_coach_info = list(team_coach_info)

    # Check if any players exist in the team
    check_teamID_formula = "SELECT * FROM PLAYER WHERE team_ID = %s"
    cursor.execute(check_teamID_formula, (teamID,))
    result = cursor.fetchall()

    if not result:
        return False, False  # Return False values if no players found

    # Roster Retrieval
    retrieve_roster_formula = ("SELECT p.playerName, p.pFName, p.pLName, p.age, r.roleName "
                               "FROM player AS p "
                               "JOIN role AS r ON p.role_ID = r.role_ID "
                               "WHERE p.team_ID = %s"
                               "ORDER BY playerName ASC")
    cursor.execute(retrieve_roster_formula, (teamID,))
    roster_list = cursor.fetchall()

    return team_coach_info, roster_list

def rteampName_DESC(teamID):
    # Coach and Team Retrieval
    retrieve_coach_team_formula = ("SELECT t.teamName, c.coachName "
                                   "FROM team AS t "
                                   "JOIN coach as c ON t.coach_ID = c.coach_ID "
                                   "WHERE t.team_ID = %s")
    cursor.execute(retrieve_coach_team_formula, (teamID,))
    team_coach_info = cursor.fetchone()

    if team_coach_info is None:
        return False, False  # Return False values if no coach or team found

    team_coach_info = list(team_coach_info)

    # Check if any players exist in the team
    check_teamID_formula = "SELECT * FROM PLAYER WHERE team_ID = %s"
    cursor.execute(check_teamID_formula, (teamID,))
    result = cursor.fetchall()

    if not result:
        return False, False  # Return False values if no players found

    # Roster Retrieval
    retrieve_roster_formula = ("SELECT p.playerName, p.pFName, p.pLName, p.age, r.roleName "
                               "FROM player AS p "
                               "JOIN role AS r ON p.role_ID = r.role_ID "
                               "WHERE p.team_ID = %s"
                               "ORDER BY playerName DESC")
    cursor.execute(retrieve_roster_formula, (teamID,))
    roster_list = cursor.fetchall()

    return team_coach_info, roster_list

def rteam_roleID_ASC(teamID):
    # Coach and Team Retrieval
    retrieve_coach_team_formula = ("SELECT t.teamName, c.coachName "
                                   "FROM team AS t "
                                   "JOIN coach as c ON t.coach_ID = c.coach_ID "
                                   "WHERE t.team_ID = %s")
    cursor.execute(retrieve_coach_team_formula, (teamID,))
    team_coach_info = cursor.fetchone()

    if team_coach_info is None:
        return False, False  # Return False values if no coach or team found

    team_coach_info = list(team_coach_info)

    # Check if any players exist in the team
    check_teamID_formula = "SELECT * FROM PLAYER WHERE team_ID = %s"
    cursor.execute(check_teamID_formula, (teamID,))
    result = cursor.fetchall()

    if not result:
        return False, False  # Return False values if no players found

    # Roster Retrieval
    retrieve_roster_formula = ("SELECT p.playerName, p.pFName, p.pLName, p.age, r.roleName "
                               "FROM player AS p "
                               "JOIN role AS r ON p.role_ID = r.role_ID "
                               "WHERE p.team_ID = %s"
                               "ORDER BY r.role_ID ASC")
    cursor.execute(retrieve_roster_formula, (teamID,))
    roster_list = cursor.fetchall()

    return team_coach_info, roster_list

def rteam_roleID_DESC(teamID):
    # Coach and Team Retrieval
    retrieve_coach_team_formula = ("SELECT t.teamName, c.coachName "
                                   "FROM team AS t "
                                   "JOIN coach as c ON t.coach_ID = c.coach_ID "
                                   "WHERE t.team_ID = %s")
    cursor.execute(retrieve_coach_team_formula, (teamID,))
    team_coach_info = cursor.fetchone()

    if team_coach_info is None:
        return False, False  # Return False values if no coach or team found

    team_coach_info = list(team_coach_info)

    # Check if any players exist in the team
    check_teamID_formula = "SELECT * FROM PLAYER WHERE team_ID = %s"
    cursor.execute(check_teamID_formula, (teamID,))
    result = cursor.fetchall()

    if not result:
        return False, False  # Return False values if no players found

    # Roster Retrieval
    retrieve_roster_formula = ("SELECT p.playerName, p.pFName, p.pLName, p.age, r.roleName "
                               "FROM player AS p "
                               "JOIN role AS r ON p.role_ID = r.role_ID "
                               "WHERE p.team_ID = %s"
                               "ORDER BY r.role_ID DESC")
    cursor.execute(retrieve_roster_formula, (teamID,))
    roster_list = cursor.fetchall()

    return team_coach_info, roster_list

def update_team_info(teamID, column, new_value):
    team_info = ['team_ID', 'teamName', 'recent_match', 'coach_ID']

    if column not in team_info:
        return False
    try:
        check_teamID_formula = "SELECT team_ID FROM TEAM WHERE team_ID = %s" # Checks if team exists
        cursor.execute(check_teamID_formula, (teamID,))
        result = cursor.fetchone()

        if column == 'team_ID':
            if result is None:
                return 'TDNE' # Team does not exist
            else:
                team_update_formula = ("UPDATE TEAM SET team_ID = %s WHERE team_ID = %s")
                player_team_update = ("UPDATE PLAYER SET team_ID = %s WHERE team_ID IS NULL")
                cursor.execute(team_update_formula, (new_value, teamID,))
                cursor.execute(player_team_update, (new_value,))
                mydb.commit()
                return 'TIUS' # Team ID Updated Successfully
        elif column == 'coach_ID':
            check_coachID_formula = "SELECT coach_ID FROM COACH WHERE coach_ID = %s" # Checks coach existence in COACH Table
            cursor.execute(check_coachID_formula, (new_value,))
            result = cursor.fetchone()

            if result is None:
                return 'CDNE' # Coach does not exists

            check_coachID_formula = "SELECT coach_ID FROM TEAM WHERE coach_ID = %s" # Checks coach in Team Table
            cursor.execute(check_coachID_formula, (new_value,))
            result = cursor.fetchone()

            if result is not None:
                return 'CAT' # Coach already takenn
            else:
                team_update_formula = ("UPDATE TEAM SET coach_ID = %s WHERE team_ID = %s")
                cursor.execute(team_update_formula, (new_value, teamID))
                mydb.commit()
                return 'CIDUS' # Coach ID Updated Successfully
        else:
            team_update_formula = ("UPDATE TEAM SET " + column + " = %s WHERE team_ID = %s")
            cursor.execute(team_update_formula, (new_value, teamID))
            mydb.commit()
            return 'TISU' # Team Information Successfully Updated
    except mysql.connector.IntegrityError as e:
        if e.errno == errorcode.ER_DUP_ENTRY:
            return "TIDAT" # Team ID already taken

def delete_team_info(teamID):
    check_ID_formula = ("SELECT team_ID FROM TEAM WHERE team_ID = %s") # Checks team existence
    cursor.execute(check_ID_formula, (teamID,))
    result = cursor.fetchone()

    if result is None:
        return 'DNE' # Does not exists
    else:
        delete_coach_formula = ("DELETE FROM TEAM WHERE team_ID = %s")
        update_team_formula = ("UPDATE PLAYER SET team_ID = NULL WHERE team_ID = %s")
        cursor.execute(delete_coach_formula, (teamID,))
        cursor.execute(update_team_formula, (teamID,))

        mydb.commit()
        return 'True' # Deletes Team

# Database Coach Table
def insert_coach(coachID, coachName, firstname, lastname):
    try:
        # Check if coachName already exists
        check_name_formula = "SELECT coach_ID FROM COACH WHERE coachName = %s"
        cursor.execute(check_name_formula, (coachName,))
        name_result = cursor.fetchone()

        if name_result is not None:
            return 'CNAE' # Coach Name already Exists

        # Check if coachID already exists
        check_id_formula = "SELECT coach_ID FROM COACH WHERE coach_ID = %s"
        cursor.execute(check_id_formula, (coachID,))
        id_result = cursor.fetchone()

        if id_result is not None:
            return 'CIDAE' # Coach ID already exists

        # Insert new coach if both checks pass
        insert_formula = "INSERT INTO COACH(coach_ID, coachName, cFName, cLName) VALUES (%s, %s, %s, %s)"
        coach = (coachID, coachName, firstname, lastname)
        cursor.execute(insert_formula, coach)
        mydb.commit()
        return True # Insertion Done

    except mysql.connector.IntegrityError as e:
        if e.errno == errorcode.ER_DUP_ENTRY:
            return 'CIDAE' # Coach ID already exists

def retrieve_coach_info(coach_ID):
    read_formula = ("SELECT * FROM COACH WHERE coach_ID = %s")
    cursor.execute(read_formula, (coach_ID,))
    coach_data = cursor.fetchone()

    if coach_data is None:
        return 'DNE' # Does not exist
    else:
        return list(coach_data) # Returns coach info as a list

def update_coach_info(coach_ID, column, new_value):
    coach_info = ['coach_ID', 'coachName', 'cFName', 'cLName']

    if column not in coach_info:
        return 'COLDNE' # Column does not exist

    try:
        check_ID_formula = ("SELECT coach_ID FROM COACH WHERE coach_ID = %s") # Checks coach ID
        cursor.execute(check_ID_formula, (coach_ID,))
        result = cursor.fetchone()

        if column == 'coach_ID':
            if result is None:
                return 'CDNE' # Coach does not exist
            else:
                check_ID_formula = ("SELECT coach_ID FROM COACH WHERE coach_ID = %s")
                cursor.execute(check_ID_formula, (new_value,))
                result = cursor.fetchone()
                coach_update_formula = ("UPDATE COACH SET " + column + " = %s WHERE coach_ID = %s")
                team_update_formula = ("UPDATE TEAM SET coach_ID = %s WHERE coach_ID IS NULL")
                # Executing the SQL UPDATE statement
                cursor.execute(coach_update_formula, (new_value, coach_ID))
                cursor.execute(team_update_formula, (new_value,))
                # Committing the transaction to apply changes to the database
                mydb.commit()
                return 'CIDUS' # Coach ID updated successfully
        else:
            coach_update_formula = ("UPDATE COACH SET " + column + " = %s WHERE coach_ID = %s")
            team_update_formula = ("UPDATE TEAM SET coach_ID = %s WHERE coach_ID IS NULL")
            # Executing the SQL UPDATE statement
            cursor.execute(coach_update_formula, (new_value, coach_ID))
            cursor.execute(team_update_formula, (new_value,))
            # Committing the transaction to apply changes to the database
            mydb.commit()
            return 'CIUS' # Coach info updated successfully
    except mysql.connector.IntegrityError as e:
        if e.errno == errorcode.ER_DUP_ENTRY:
            return 'CAT' # Coach already taken

def delete_coach_info(coach_ID):
    check_ID_formula = ("SELECT coach_ID FROM COACH WHERE coach_ID = %s") # Checks coach existence
    cursor.execute(check_ID_formula, (coach_ID, ))
    result = cursor.fetchone()

    if result is None:
        return 'DNE' # Coach does not exist
    else:
        delete_coach_formula = ("DELETE FROM COACH WHERE coach_ID = %s")
        update_team_formula = ("UPDATE TEAM SET coach_ID = NULL WHERE coach_ID = %s")
        cursor.execute(delete_coach_formula, (coach_ID,))
        cursor.execute(update_team_formula, (coach_ID,))

        mydb.commit()
        return 'True' # Successfully deletes coach from DB