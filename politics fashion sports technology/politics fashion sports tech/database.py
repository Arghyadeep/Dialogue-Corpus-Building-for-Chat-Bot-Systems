import csv
import pandas as pd

level = int(input("Enter total number of CSV files: "))
input_arr = []

print("Enter CSV file names in order starting from the first: ")
for i in range(level):
    input_file = input("Enter input filename(with .csv extension): ")
    input_arr.append(input_file)

data = []
for j in range(level):
    df = pd.read_csv(input_arr[j])
    data.append(df)

texts = []
dialogueacts = []
uniqueID = []


for i in range (len(input_arr)):
    for j in range(len(data[i])):
        if i == 0:
            texts.append("Let's talk about "+str(data[0]['Input.slot0'][j]))
            dialogueacts.append('prompt')
            texts.append(data[0]['Answer.general'][j])
            dialogueacts.append('General')
            texts.append(data[0]['Answer.question'][j])
            dialogueacts.append('Question')
            texts.append(data[0]['Answer.similar'][j])
            dialogueacts.append('Similar')
            texts.append(data[0]['Answer.specific'][j])
            dialogueacts.append('Specific')
        
        else:
            texts.append(data[i]['Answer.change'][j])
            dialogueacts.append('change')
            texts.append(data[i]['Answer.joking_sarcastic'][j])
            dialogueacts.append('joking_sarcastic')
            texts.append(data[i]['Answer.more_detail'][j])
            dialogueacts.append('More_detail')
            texts.append(data[i]['Answer.sympathetic'][j])
            dialogueacts.append('Sympathetic')
            

for i in range(1,len(texts)+1):
    uniqueID.append(str((5 - len(str(i)))*'0'+str(i)))
    
header = ['UniqueID','DialogueActs','Texts']
columns = []
columns.append(uniqueID)
columns.append(dialogueacts)
columns.append(texts)

with open('database.csv','w',newline='') as file:
    writer = csv.writer(file,delimiter=',')
    writer.writerows([header])
    writer.writerows(zip(*columns))
file.close()

