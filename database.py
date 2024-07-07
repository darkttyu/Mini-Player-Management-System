import mysql.connector
from mysql.connector import errorcode

# Minor adjustments to be completed
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

# Database Admin Table
def check_admin(username, password):
    login_formula = ("SELECT * FROM admin WHERE admin_user = %s AND password = %s")
    cursor.execute(login_formula, (username, password))
    retrieve_admin = cursor.fetchone()

    if retrieve_admin is None:
        return False
    else:
        return True

# Database Player Performance Table
def insert_playerstat_info(name, year, games, most_used, wr, participation):
    check_formula = ("SELECT playerName, year FROM PLAYER_PERFORMANCE WHERE playerName = %s AND year = %s")
    cursor.execute(check_formula, (name, year))
    result = cursor.fetchone()

    if result is None:
        insert_formula = ("INSERT INTO PLAYER_PERFORMANCE (playerName, year, games_played, "
                          "most_used, win_rate, player_participation) "
                          "VALUES (%s, %s, %s, %s, %s, %s)")
        cursor.execute(insert_formula, (name, year, games, most_used, wr, participation))

        mydb.commit()
        print("Player Statistics Inserted Successfully!")
    else:
        print("Cannot Insert Data. Player Statistics already exists!")

def retrieve_playerstat_info(name, year):
    retrieve_player_formula = ("SELECT * FROM player_performance WHERE playerName = %s AND year = %s")
    cursor.execute(retrieve_player_formula, (name, year))
    retrieved_player = cursor.fetchone()

    if retrieved_player is None:
        print("Cannot Retrieve Player Stats. Information for that player/year does not exist.")
    else:
        print(f"Player Name: {retrieved_player[1]}")
        print(f"Year: {retrieved_player[2]}")
        print(f"Games Played: {retrieved_player[3]}")
        print(f"Most Used Champion: {retrieved_player[4]}")
        print(f"Win Rate: {retrieved_player[5]}")
        print(f"Player Participation: {retrieved_player[6]}")

def update_playerstat_info(name, year, column, new_value):
    player_stat_list = ['games_played', 'most_used', 'win_rate', 'player_participation']

    # Check if the specified column is valid
    if column not in player_stat_list:
        print("Invalid Column")
        return

    # Convert new_value to the appropriate type
    if column == 'win_rate' or column == 'player_participation':
        new_value = float(new_value)

    # Check if the player exists
    check_player_formula = ("SELECT * FROM PLAYER WHERE playerName = %s")
    cursor.execute(check_player_formula, (name,))
    player_info = cursor.fetchone()

    if player_info is None:
        print("Cannot Update Data. Player does not exist.")
        return

    # Check if the player statistics exist for the given year
    check_playerstat_formula = ("SELECT * FROM PLAYER_PERFORMANCE WHERE playerName = %s AND year = %s")
    cursor.execute(check_playerstat_formula, (name, year))
    player_stat = cursor.fetchone()

    if player_stat is None:
        print("Cannot Update Data. Player statistics do not exist.")
        return

    # Update player statistics
    update_playerstat_formula = ("UPDATE PLAYER_PERFORMANCE SET " + column + " = %s WHERE playerName = %s AND year = %s")
    cursor.execute(update_playerstat_formula, (new_value, name, year))
    mydb.commit()
    print("Player Statistic Successfully Updated!")

def delete_player_statinfo(name, year):
    delete_player_formula = "DELETE FROM PLAYER_PERFORMANCE WHERE playerName = %s AND year = %s"
    cursor.execute(delete_player_formula, (name, year))
    mydb.commit()

    print("Player Statistics Successfully Deleted.")

# Database Player Table

def insert_player(IGN, FName, LName, age, role_ID, team_ID):
    # Checks if a player already exists in the database
    check_IGN_formula = ("SELECT playerName FROM PLAYER WHERE playerName = %s")
    cursor.execute(check_IGN_formula, (IGN,))
    IGN_result = cursor.fetchone()

    check_teamCount_formula = ("SELECT COUNT(team_ID) FROM PLAYER WHERE team_ID = %s")
    cursor.execute(check_teamCount_formula, (team_ID,))
    count_result = cursor.fetchone()

    if count_result[0] <= 5:
        if IGN_result is None:
            insert_formula = ("INSERT INTO PLAYER (playerName, pFName, PLName, age, role_ID, team_ID"
                              ") VALUES (%s, %s, %s, %s, %s, %s)")
            player = (IGN, FName, LName, age, role_ID, team_ID)

            # Executing the SQL INSERT statement
            cursor.execute(insert_formula, player)

            # Committing the transaction to apply changes to the database
            mydb.commit()
            return True
        else:
            return 'PLAE'
    else:
        return 'MAX'

def read_player_info(IGN):
    check_IGN_formula = ("SELECT playerName FROM PLAYER WHERE playerName = %s")
    cursor.execute(check_IGN_formula, (IGN, ))

    result = cursor.fetchone()

    if result is None:
        return 'PLDNE'
    else:
        retrieve_player_formula = ("SELECT p.playerName, p.pFName, p.pLName, p.age, "
                                   "r.roleName, t.teamName, c.coachName "
                                   "FROM player AS p "
                                   "JOIN role AS r ON p.role_ID = r.role_ID "
                                   "JOIN team AS t ON p.team_ID = t.team_ID "
                                   "JOIN coach AS c ON t.coach_ID = c.coach_ID "
                                   "WHERE p.playerName = %s")
        cursor.execute(retrieve_player_formula, (IGN, ))
        retrieved_info = cursor.fetchone()
        return retrieved_info

def update_player_info(IGN, column, new_value):
    column_list = ['playerName', 'pFName', 'pLName', 'age', 'role_ID', 'team_ID']

    # Checking if the specified column is valid
    if column not in column_list:
        return 'CDNE'

    check_player = "SELECT playerName FROM PLAYER WHERE playerName = %s"
    cursor.execute(check_player, (IGN,))
    result = cursor.fetchone()

    if result is None:
        return 'PDNE'

    if column == 'playerName':
        update_player = ("UPDATE PLAYER SET playerName = %s WHERE playerName = %s")
        update_player_stat = ("UPDATE PLAYER_PERFORMANCE SET playerName %s WHERE playerName IS NULL")
        cursor.execute(update_player, (new_value, IGN,))
        cursor.execute(update_player_stat, (new_value))
        mydb.commit()
        return 'PNUS'

    elif column == 'team_ID':
        checkteam_ID = ("SELECT team_ID FROM TEAM WHERE team_ID = %s")
        cursor.execute(checkteam_ID, (new_value,))
        result = cursor.fetchone()

        if result is None:
            return 'TDNE'

        check_teamcount = ("SELECT COUNT(*) FROM PLAYER WHERE team_ID = %s")
        cursor.execute(check_teamcount, (new_value,))
        result = cursor.fetchone()

        if result[0] >= 6:
            return 'MAX'
        else:
            update_teamID = ("UPDATE PLAYER SET team_ID = %s WHERE playerName = %s")
            cursor.execute(update_teamID, (new_value, IGN))
            mydb.commit()
            return 'PTIDUS'
    else:
        update_player = ("UPDATE PLAYER SET " + column + " = %s WHERE playerName = %s")
        cursor.execute(update_player, (new_value, IGN))
        mydb.commit()
        return 'PIUS'

def delete_player_info(name):
    check_player = ("SELECT playerName FROM PLAYER WHERE playerName = %s")
    cursor.execute(check_player, (name, ))
    result = cursor.fetchone()

    if result is None:
        return 'PDNE'
    else:
        delete_player_formula = ("DELETE FROM PLAYER WHERE playerName = %s")
        cursor.execute(delete_player_formula, (name, ))
        mydb.commit()
        return True

# Database Team Table
def insert_team(team_id, team_name, recent_match, coach_ID):

    try:
        check_teamID = ("SELECT team_ID FROM TEAM WHERE team_ID = %s")
        cursor.execute(check_teamID, (team_id,))
        result = cursor.fetchone()

        if result is not None:
            return 'TIDAE'

        # Checks if a team already exists in the database
        check_team = ("SELECT teamName FROM TEAM WHERE teamName = %s")
        cursor.execute(check_team, (team_name,))
        result = cursor.fetchone()

        if result is not None:
            return 'TNAE'

        check_coach = ("SELECT coach_ID FROM TEAM WHERE coach_ID = %s")
        cursor.execute(check_coach, (coach_ID,))
        result = cursor.fetchone()

        if result is not None:
            return 'CAT'

        insert_formula = ("INSERT INTO TEAM (team_ID, teamName, recent_match, coach_ID) VALUES (%s, %s, %s, %s)")
        team = (team_id, team_name, recent_match, coach_ID)

        # Executing the SQL INSERT statement
        cursor.execute(insert_formula, team)

        # Committing the transaction to apply changes to the database
        mydb.commit()
        return 'TIS'

    except mysql.connector.IntegrityError as e:
        if e.errno == errorcode.ER_DUP_ENTRY:
            return 'TIDAE'

def retrieve_roster_info(teamID):
    check_teamID_formula = ("SELECT * FROM PLAYER WHERE team_ID = %s")
    cursor.execute(check_teamID_formula, (teamID, ))
    result = cursor.fetchall()

    if result is None:
        return False # To be Updated
    else:
        # Roster Retrieval
        retrieve_roster_formula = ("SELECT p.playerName, p.pFName, p.pLName, p.age, r.roleName "
                                   "FROM player AS p "
                                   "JOIN role AS r ON p.role_ID = r.role_ID "
                                   "WHERE p.team_ID = %s ")
        cursor.execute(retrieve_roster_formula, (teamID,))
        roster_list = cursor.fetchall()

        # Coach and Team Retrieval
        retrieve_coach_team_formula = ("SELECT t.teamName, c.coachName "
                                       "FROM team AS t "
                                       "JOIN coach as c ON t.coach_ID = c.coach_ID "
                                       "WHERE t.team_ID = %s ")
        cursor.execute(retrieve_coach_team_formula, (teamID, ))
        team_coach_info = list(cursor.fetchone())

        print(team_coach_info)
        print(roster_list)

def update_team_info(teamID, column, new_value):
    team_info = ['team_ID', 'teamName', 'recent_match', 'coach_ID']

    if column not in team_info:
        return False
    try:
        check_teamID_formula = "SELECT team_ID FROM TEAM WHERE team_ID = %s"
        cursor.execute(check_teamID_formula, (teamID,))
        result = cursor.fetchone()

        if column == 'team_ID':
            new_value = int(new_value)
            if result is None:
                return 'TDNE'
            else:
                check_teamID_formula = "SELECT team_ID FROM TEAM WHERE team_ID = %s"
                cursor.execute(check_teamID_formula, (new_value,))
                result = cursor.fetchone()
                team_update_formula = ("UPDATE TEAM SET team_ID = %s WHERE team_ID = %s")
                player_team_update = ("UPDATE PLAYER SET team_ID = %s WHERE team_ID IS NULL")
                cursor.execute(team_update_formula, (new_value, teamID,))
                cursor.execute(player_team_update, (new_value,))
                mydb.commit()
                return 'TIUS'
        elif column == 'coach_ID':

            check_coachID_formula = "SELECT coach_ID FROM COACH WHERE coach_ID = %s"
            cursor.execute(check_coachID_formula, (new_value,))
            result = cursor.fetchone()

            if result is None:
                return 'CDNE'

            check_coachID_formula = "SELECT coach_ID FROM TEAM WHERE coach_ID = %s"
            cursor.execute(check_coachID_formula, (new_value,))
            result = cursor.fetchone()

            if result is not None:
                return 'CAT'
            else:
                team_update_formula = ("UPDATE TEAM SET coach_ID = %s WHERE team_ID = %s")
                cursor.execute(team_update_formula, (new_value, teamID))
                mydb.commit()
                return 'CIDUS'
        else:
            team_update_formula = ("UPDATE TEAM SET " + column + " = %s WHERE team_ID = %s")
            cursor.execute(team_update_formula, (new_value, teamID))
            mydb.commit()
            return 'TISU'
    except mysql.connector.IntegrityError as e:
        if e.errno == errorcode.ER_DUP_ENTRY:
            return "TIDAT"

def delete_team_info(teamID):
    check_ID_formula = ("SELECT team_ID FROM TEAM WHERE team_ID = %s")
    cursor.execute(check_ID_formula, (teamID,))
    result = cursor.fetchone()

    if result is None:
        return 'DNE'
    else:
        delete_coach_formula = ("DELETE FROM TEAM WHERE team_ID = %s")
        update_team_formula = ("UPDATE PLAYER SET team_ID = NULL WHERE team_ID = %s")
        cursor.execute(delete_coach_formula, (teamID,))
        cursor.execute(update_team_formula, (teamID,))

        mydb.commit()
        return 'True'

# Database Coach Table
def insert_coach(coachID, coachName, firstname, lastname):
    try:
        # Check if coachName already exists
        check_name_formula = "SELECT coach_ID FROM COACH WHERE coachName = %s"
        cursor.execute(check_name_formula, (coachName,))
        name_result = cursor.fetchone()

        if name_result is not None:
            return 'CNAE'

        # Check if coachID already exists
        check_id_formula = "SELECT coach_ID FROM COACH WHERE coach_ID = %s"
        cursor.execute(check_id_formula, (coachID,))
        id_result = cursor.fetchone()

        if id_result is not None:
            return 'CIDAE'

        # Insert new coach if both checks pass
        insert_formula = "INSERT INTO COACH(coach_ID, coachName, cFName, cLName) VALUES (%s, %s, %s, %s)"
        coach = (coachID, coachName, firstname, lastname)
        cursor.execute(insert_formula, coach)
        mydb.commit()
        return True

    except mysql.connector.IntegrityError as e:
        if e.errno == errorcode.ER_DUP_ENTRY:
            return 'CIDAE'

def retrieve_coach_info(coach_ID):
    read_formula = ("SELECT * FROM COACH WHERE coach_ID = %s")
    cursor.execute(read_formula, (coach_ID,))
    coach_data = cursor.fetchone()

    if coach_data is None:
        return 'DNE'
    else:
        return list(coach_data)

def update_coach_info(coach_ID, column, new_value):
    coach_info = ['coach_ID', 'coachName', 'cFName', 'cLName']

    if column not in coach_info:
        return 'COLDNE'

    try:
        check_ID_formula = ("SELECT coach_ID FROM COACH WHERE coach_ID = %s")
        cursor.execute(check_ID_formula, (coach_ID,))
        result = cursor.fetchone()

        if column == 'coach_ID':
            new_value = int(new_value)
            if result is None:
                return 'CDNE'
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
                return 'CIDUS'
        else:
            coach_update_formula = ("UPDATE COACH SET " + column + " = %s WHERE coach_ID = %s")
            team_update_formula = ("UPDATE TEAM SET coach_ID = %s WHERE coach_ID IS NULL")
            # Executing the SQL UPDATE statement
            cursor.execute(coach_update_formula, (new_value, coach_ID))
            cursor.execute(team_update_formula, (new_value,))
            # Committing the transaction to apply changes to the database
            mydb.commit()
            return 'CIUS'
    except mysql.connector.IntegrityError as e:
        if e.errno == errorcode.ER_DUP_ENTRY:
            return 'CAT'

def delete_coach_info(coach_ID):
    check_ID_formula = ("SELECT coach_ID FROM COACH WHERE coach_ID = %s")
    cursor.execute(check_ID_formula, (coach_ID, ))
    result = cursor.fetchone()

    if result is None:
        return 'DNE'
    else:
        delete_coach_formula = ("DELETE FROM COACH WHERE coach_ID = %s")
        update_team_formula = ("UPDATE TEAM SET coach_ID = NULL WHERE coach_ID = %s")
        cursor.execute(delete_coach_formula, (coach_ID,))
        cursor.execute(update_team_formula, (coach_ID,))

        mydb.commit()
        return 'True'