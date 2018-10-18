import mysql.connector

db = mysql.connector.connect(host ='localhost',
                     user ='root',
                     passwd ='Arghya1990',
                     database ='ChatBot' )

# prepare a cursor object using cursor() method
cursor = db.cursor()

table1 = "Conversation(Utterance_ID INT(5) PRIMARY KEY, Conversation_ID INT(5), No_Turns INT(2), Turn_ID INT(2))"

# create table1
cursor.execute("CREATE TABLE IF NOT EXISTS "+ table1)

table2 = "Utterances(Unique_ID INT(5) PRIMARY KEY, Dialogue_Act VARCHAR(255), Texts TEXT, FOREIGN KEY(Unique_ID) REFERENCES Conversation(Utterance_ID))"

# create table2
cursor.execute("CREATE TABLE IF NOT EXISTS "+ table2)

table3 = "HIT(Utterance_ID INT(5) PRIMARY KEY, HITType_ID VARCHAR(255), HIT_ID VARCHAR(255), FOREIGN KEY(Utterance_ID) REFERENCES Conversation(Utterance_ID))"

# create table3
cursor.execute("CREATE TABLE IF NOT EXISTS "+ table3)



cursor.execute("SHOW TABLES")

for x in cursor:
    print(x)
