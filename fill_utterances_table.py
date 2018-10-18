import mysql.connector

db = mysql.connector.connect(host ='localhost',
                     user ='root',
                     passwd ='Arghya1990',
                     database ='ChatBot' )

# prepare a cursor object using cursor() method
cursor = db.cursor()

sql = """INSERT INTO Utterances (Unique_ID, Dialogue_Act, Texts) VALUES (%s,%s,%s);"""

utterances_vals = []

import pandas as pd

data1 = pd.read_csv("utterance.csv", encoding = 'latin1')

for i in range(len(data1)):
    temp1 = int(data1['UniqueID'][i])
    temp2 = str(data1['DialogueActs'][i])
    temp3 = str(data1['Texts'][i])
    


    temp = [temp1,temp2,temp3]

    utterances_vals.append(tuple(temp))

    

#print(utterances_vals[0])
cursor.executemany(sql,utterances_vals)

db.commit()

print(cursor.rowcount, "was inserted.")


    
