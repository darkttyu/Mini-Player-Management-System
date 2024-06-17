import mysql.connector

mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    password='DroU9HPwqRHnzOC',
    port='3307',
    database='player_management'
)

cursor = mydb.cursor()

def insert_player(playername, age, role, winrate, recentlyused, mostused, teamparticipation, teamid):
    insert_formula = ("INSERT INTO players (playername, age, role, win_rate, recently_used, most_used, "
                  "team_participation, teamID) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)")
    player = (playername, age, role, winrate, recentlyused, mostused, teamparticipation, teamid)
    cursor.execute(insert_formula, player)
    mydb.commit()

def retrieve_player(name):
    read_formula = ("SELECT playerName, age, role, "
                    "win_rate, recently_used, most_used, "
                    "team_participation, teamName, recent_match "
                    "FROM PLAYERS INNER JOIN "
                    "TEAMS ON PLAYERS.TEAMID = TEAMS.TEAMID "
                    "WHERE playername = %s")
    cursor.execute(read_formula, (name,))
    player_data = cursor.fetchone()
    pdata_list = list(player_data)

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

def update_player(name, column):
    column_list = ['playerName', 'age', 'role', 'win_rate', 'recent_used', 'most_used', 'team_participation']

    if column not in column_list:
        print("Invalid Column")
        return
    elif column == 'win_rate' or column == 'team_participation':
        new_value = float(input("Enter New Value: "))
    elif column == 'age':
        new_value = int(input("Enter new Value: "))
    else:
        new_value = input("Enter New Value: ")

    update_formula = ("UPDATE PLAYERS "
                      "SET " + column + " = %s "
                      "WHERE playerName = %s")
    cursor.execute(update_formula, (new_value, name))
    print("Table Updated Successfully!")
    mydb.commit()

def delete_player(name):
    delete_formula = ("DELETE FROM PLAYERS WHERE playerName = %s")
    cursor.execute(delete_formula, (name,))
    print("Player Deleted Successfully!")
    mydb.commit()