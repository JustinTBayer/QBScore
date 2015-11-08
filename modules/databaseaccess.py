from PyQt4.QtSql import *
from PyQt4.QtGui import QImage, QPixmap

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
    query = QSqlQuery("SELECT team_id FROM team WHERE name = '" + team + "'")
    teamId = query.record().indexOf("team_id")
    teamList = []
    while (query.next()):
        teamList.append(query.value(teamId).toString())
        
    print "this is the teamlist",  teamList
    query = QSqlQuery("SELECT * FROM player WHERE teamId = '" + teamList[0] + "'")
    playerId = query.record().indexOf("name")
    players1List = []
    while (query.next()):
        players1List.append(query.value(playerId).toString())
    return players1List
    
def get_Player_Name_By_Id(id):
    query = QSqlQuery("SELECT name FROM player WHERE playerId = " + str(id))
    query.next()
    name = query.record().indexOf("name")
    print name
    return name

def get_Team_Pic(team):
    query = QSqlQuery ("SELECT * FROM team WHERE name = '" +team + "'")
    query.next()
    picIndex = query.record().indexOf("Picture")
    picture = query.value(picIndex).toByteArray()
    picturePixmap = QPixmap()
    picturePixmap.loadFromData(picture)
    return picturePixmap
