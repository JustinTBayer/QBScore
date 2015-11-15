from PyQt4.QtSql import *
from PyQt4.QtGui import QImage, QPixmap

db = QSqlDatabase.addDatabase("QMYSQL")

db.setHostName("localhost")
db.setDatabaseName("quizbowl")
db.setUserName("quizbowl")
db.setPassword("password")

if (db.open()==False):     
  print db.lastError().text()

def get_Teams ():
    query = QSqlQuery ("SELECT * FROM team LIMIT 5")
    team_id = query.record().indexOf("team_id")
    name = query.record().indexOf("name")
    teamsDict = {}
    while (query.next()):
        teamsDict[query.value(team_id).toString()] = query.value(name).toString()
    print teamsDict
    return teamsDict
    
def get_Player_Name_By_Team_Id(team_id):
    query = QSqlQuery("SELECT * FROM player WHERE teamId = '" + team_id + "'")
    playerId = query.record().indexOf("name")
    players1List = []
    while (query.next()):
        players1List.append(query.value(playerId).toString())
    return players1List

def get_Player_Id_By_Team_Id(team_id):
    query = QSqlQuery("SELECT * FROM player WHERE teamId = '" + team_id + "'")
    playerId = query.record().indexOf("playerId")
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

def get_Question_By_Id(question_id):
    query = QSqlQuery("SELECT Question, Answer FROM questionsandanswers WHERE questionId = " + str(question_id))
    query.next()
    question_index = query.record().indexOf("Question")
    answer_index = query.record().indexOf("Answer")
    question = query.value(question_index).toString()
    answer = query.value(answer_index).toString()
    qaList = [question, answer]
    return qaList

def submit_Score(self, points):
    query = QSqlQuery()
    query.prepare("INSERT INTO gamedetails (gameId, tossup, playerId, points) " "VALUES (:gameId, :tossup, :playerId, :points);")
    query.bindValue(":gameId", self.gameId)
    query.bindValue(":tossup",  self.questionNumber)
    query.bindValue(":playerId", self.currentBuzzedPlayerId)
    query.bindValue(":points",  points)
    query.exec_()
