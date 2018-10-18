import mysql.connector

db = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = 'Arghya1990'
    )


cursor = db.cursor()

cursor.execute("create database IF NOT EXISTS ChatBot")

# Commit your changes in the database
db.commit()

# disconnect from server
db.close()

db = MySQLdb.connect(host ='localhost',
                     user ='root',
                     passwd ='Arghya1990',
                     database ='ChatBot' )

# prepare a cursor object using cursor() method
cursor = db.cursor()



cursor.execute("SHOW TABLES")

for x in cursor:
    print(x)
