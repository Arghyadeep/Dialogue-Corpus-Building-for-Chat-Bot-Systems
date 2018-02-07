import pandas as pd
import csv
files = int(input("Enter total number of CSV files: "))
input_arr = []

print("Enter CSV file names in order starting from the first: ")
for i in range(files):
    input_file = input("Enter input filename(with .csv extension): ")
    input_arr.append(input_file)

data = []
for j in range(files):
    df = pd.read_csv(input_arr[j])
    data.append(df)

texts = []
dialogueacts = []
uniqueID = []

counter = -1
for i in range(11485):
    counter +=1
    uniqueID.append(counter)
    
    

for i in range(4):
    for j in range(len(data[i])):
        texts.append("I really like " +str(data[i]['Input.slot0'][j]))
        dialogueacts.append('prompt')
        texts.append(data[i]['Answer.general'][j])
        dialogueacts.append('General')
        texts.append(data[i]['Answer.question'][j])
        dialogueacts.append('Question')
        texts.append(data[i]['Answer.similar'][j])
        dialogueacts.append('Similar')
        texts.append(data[i]['Answer.specific'][j])
        dialogueacts.append('Specific')

for i in range(4,8):
    for j in range(len(data[i])):
        texts.append(str(data[i]['Input.slot0'][j]))
        dialogueacts.append('prompt')
        texts.append(data[i]['Answer.Your_Response'][j])
        dialogueacts.append('General Response')

for j in range(len(data[8])):
    texts.append(str(data[8]['Input.slot0'][j]) + str(data[8]['Input.slot1'][j]))
    dialogueacts.append('prompt')
    texts.append(data[8]['Answer.general'][j])
    dialogueacts.append('General')
    texts.append(data[8]['Answer.question'][j])
    dialogueacts.append('Question')
    texts.append(data[8]['Answer.similar'][j])
    dialogueacts.append('Similar')
    texts.append(data[8]['Answer.specific'][j])
    dialogueacts.append('Specific')

for j in range(len(data[9])):
    texts.append("I really " + str(data[9]['Input.slot0'][j]) +str(data[9]['Input.slot1'][j]))
    dialogueacts.append('prompt')
    texts.append(data[9]['Answer.general'][j])
    dialogueacts.append('General')
    texts.append(data[9]['Answer.question'][j])
    dialogueacts.append('Question')
    texts.append(data[9]['Answer.similar'][j])
    dialogueacts.append('Similar')
    texts.append(data[9]['Answer.specific'][j])
    dialogueacts.append('Specific')



utterance_ID = uniqueID
no_of_turns = []
for i in range(len(uniqueID)):
    no_of_turns.append(1)
    
turn_ID = [None]*len(uniqueID)
for i in range(len(uniqueID)):
    if dialogueacts[i] == 'prompt':
        turn_ID[i] = 0
    else:
        turn_ID[i] = 1


conv_ID = []
counter = -1
for i in range(63):
    counter +=1
    for j in range(5):
        conv_ID.append(counter)

for i in range(5060):
    counter +=1
    for j in range(2):
        conv_ID.append(counter)

for i in range(210):
    counter +=1
    for j in range(5):
        conv_ID.append(counter)
        

HIT_ID = [None]*len(uniqueID)
HITTypeID = [None]*len(uniqueID)

counter = 0

hit = []
hittype = []

for i in range((files)):
    for j in range(len(data[i])):
        hit.append(data[i]['HITId'][j])
        hittype.append(data[i]['HITTypeId'][j])

counter = 0
for i in range(63):
    for j in range(5):
        counter += 1
        if counter%5 == 0:
            counter +=1
        HIT_ID[counter]=hit[i]
        HITTypeID[counter]=hittype[i]

       
for i in range(63,5060+63):
    for j in range(2):
        if j == 1:
            HIT_ID[counter]=hit[i]
        HITTypeID[counter]=hittype[i]


for i in range(63 + 5060,5060+63+210):
    for j in range(5):
        counter += 1
        if counter%5 == 0:
            counter +=1
        HIT_ID[counter]=hit[i]
        HITTypeID[counter]=hittype[i]

for i in range(len(uniqueID)):
    if HIT_ID[i] == None:
        HIT_ID[i] = 'NA'
    if HITTypeID [i] == None:
        HITTypeID[i] = 'NA'

        
header1 = ['UniqueID','DialogueActs','Texts']
columns1 = []
columns1.append(uniqueID)
columns1.append(dialogueacts)
columns1.append(texts)

with open('database.csv','w',newline='') as file:
    writer = csv.writer(file,delimiter=',')
    writer.writerows([header1])
    writer.writerows(zip(*columns1))
file.close()


header2 = ['Utterance_ID','Conversation_ID','No_Of_Turns','Turn_ID']
columns2 = []
columns2.append(uniqueID)
columns2.append(conv_ID)
columns2.append(no_of_turns)
columns2.append(turn_ID)

with open('conversation.csv','w',newline='') as file:
    writer = csv.writer(file,delimiter=',')
    writer.writerows([header2])
    writer.writerows(zip(*columns2))
file.close()

header3 = ['Utterance_ID','HITTypeID','HIT_ID']
columns3 = []
columns3.append(uniqueID)
columns3.append(HITTypeID)
columns3.append(HIT_ID)

with open('HIT.csv','w',newline='') as file:
    writer = csv.writer(file,delimiter=',')
    writer.writerows([header3])
    writer.writerows(zip(*columns3))
file.close()
           



        
