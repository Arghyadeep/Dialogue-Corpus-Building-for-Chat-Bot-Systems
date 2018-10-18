import mysql.connector

db = mysql.connector.connect(host ='localhost',
                     user ='root',
                     passwd ='Arghya1990',
                     database ='ChatBot' )

# prepare a cursor object using cursor() method
cursor = db.cursor()

sql = """INSERT INTO Conversation (Utterance_ID, Conversation_ID, No_Turns, Turn_ID) VALUES (%s,%s,%s,%s);"""

conversation_vals = []

import pandas as pd

data1 = pd.read_csv("conversation.csv", encoding = 'latin1')

for i in range(len(data1)):
    temp1 = int(data1['Utterance_ID'][i])
    temp2 = int(data1['Conversation_ID'][i])
    temp3 = int(data1['No_Of_Turns'][i])
    temp4 = int(data1['Turn_ID'][i])


    temp = [temp1,temp2,temp3,temp4]

    cursor.execute(sql,temp)

    db.commit()




print(cursor.rowcount, "was inserted.")

    
