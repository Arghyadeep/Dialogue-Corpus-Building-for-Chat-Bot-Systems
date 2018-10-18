import mysql.connector

db = mysql.connector.connect(host ='localhost',
                     user ='root',
                     passwd ='Arghya1990',
                     database ='ChatBot' )

# prepare a cursor object using cursor() method
cursor = db.cursor()

sql = """INSERT INTO HIT (Utterance_ID, HITType_ID, HIT_ID) VALUES (%s,%s,%s);"""

hit_vals = []

import pandas as pd

data1 = pd.read_csv("HIT.csv", encoding = 'latin1')

for i in range(len(data1)):
    temp1 = int(data1['Utterance_ID'][i])
    temp2 = str(data1['HITTypeID'][i])
    temp3 = str(data1['HIT_ID'][i])
    


    temp = [temp1,temp2,temp3]

    hit_vals.append(tuple(temp))

    

print(hit_vals[0])
cursor.executemany(sql,hit_vals)

db.commit()

print(cursor.rowcount, "was inserted.")


