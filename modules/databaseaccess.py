from PyQt4.QtSql import *

db = QSqlDatabase.addDatabase("QMYSQL")

db.setHostName("localhost")
db.setDatabaseName("quizbowl")
db.setUserName("apo")
db.setPassword("dbPW")

if (db.open()==False):     
  print db.lastError().text()

def get_Teams ():
    query = QSqlQuery ("SELECT * FROM team LIMIT 5")
    name = query.record().indexOf("name")
    teamsList = [""]
    while (query.next()):
        teamsList.append(query.value(name).toString())
    return teamsList

def get_Players_By_Team(team):
    query = QSqlQuery("SELECT teamId FROM team WHERE name = '" + team + "'")
    teamId = query.record().indexOf("teamId")
    teamList = []
    while (query.next()):
        teamList.append(query.value(teamId).toString())
        
    print "this is the teamlist",  teamList
    query = QSqlQuery("SELECT playerId FROM player WHERE teamId = '" + teamList[0] + "'")
    playerId = query.record().indexOf("playerId")
    players1List = []
    while (query.next()):
        players1List.append(query.value(playerId).toString())
    
    return players1List
    
def get_Player_Name_By_Id(playerId):
    query = QSqlQuery("SELECT name FROM player WHERE playerId = " + playerId)
    name = query.record().indexOf("name")
    return name
