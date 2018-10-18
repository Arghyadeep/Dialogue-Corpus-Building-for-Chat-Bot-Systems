import mysql.connector

db = mysql.connector.connect(host ='localhost',
                     user ='root',
                     passwd ='Arghya1990',
                     database ='ChatBot' )

# prepare a cursor object using cursor() method
cursor = db.cursor()



"""
Find all utterances that have no turns follwoing them
(i.e. were not selected for further annotation)
"""

sql1 = "SELECT a.Unique_ID,\
    a.Texts\
    FROM\
    Utterances a Join Conversation b\
    On a.Unique_ID = b.Utterance_ID\
    Where b.No_Turns = 1 and b.Turn_ID = 1"

cursor.execute(sql1)

result1 = cursor.fetchall()


"""
Given some keyword find all utterances that contain that keyword
"""


sql2 = "SELECT\
    a.Unique_ID, a.Texts\
    FROM\
    Utterances a\
    WHERE\
    a.Texts LIKE '%movie%'"

cursor.execute(sql2)

result2 = cursor.fetchall()


"""
Given some Utterance(ID or text), find the number
of conversations that it occurs in
"""

unique_ID = str(15)
text = "I really like Star Wars"

sql3 = "(SELECT COUNT(Conversation_ID)\
    FROM\
    Utterances a JOIN Conversation b\
    On a.Unique_ID = b.Utterance_ID\
    WHERE\
    a.Texts =" + '"' + text + '"' +"\
    OR\
    a.Unique_ID =" + '"' + unique_ID+ '"' +")"
    

cursor.execute(sql3)

result3 = cursor.fetchall()

"""
Given some utterance(ID or text), get all next turns that it is
a parent of(i.e. all that comes after it)
"""

text = "I love Star Wars"
Unique_ID = str(15)

sql4 = "SELECT\
    a.Unique_ID, a.Texts\
    FROM\
    Utterances a JOIN Conversation b\
    ON a.Unique_ID = b.Utterance_ID\
    WHERE\
    b.Conversation_ID = ANY\
    (Select b.Conversation_ID\
    FROM\
    Utterances a JOIN Conversation b\
    ON a.Unique_ID = b.Utterance_ID\
    WHERE\
    a.Texts =" + '"' + text + '"' +"\
    OR\
    a.Unique_ID = " + '"' + unique_ID+ '"' +")" + "AND\
    b.Turn_ID > ANY(SELECT\
        b.Turn_ID\
        FROM\
        Utterances a JOIN Conversation b\
        ON a.Unique_ID = b.Utterance_ID\
        WHERE\
        a.Texts =" + '"' + text + '"' +"\
        OR\
        a.Unique_ID =" + '"' + unique_ID + '"' + ")"
    

cursor.execute(sql4)

result4 = cursor.fetchall()

for i in range(2):
    print(result4[i])
