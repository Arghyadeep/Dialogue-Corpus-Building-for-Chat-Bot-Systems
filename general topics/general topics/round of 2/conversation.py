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


datacomp = pd.read_csv('database1.csv')

utt_id = [i for i in range(1,len(datacomp)+1)]
conv = 0
conv_id = [None]*len(datacomp)
turn = 0
turn_id = [None]*len(datacomp)
no_turns = [None]*len(datacomp)

counter=0
for i in range(len(data[0])*5):
    if i>0 and i%5 == 0:
        counter += 1
    conv_id[i]=counter
    turn_id[i]=1

for i in range(len(datacomp)):
    if datacomp['DialogueActs'][i]=='prompt':
        turn_id[i] = 0
    
temp =''

for j in range(len(data[0])*5):
    if j%5 != 0:
        temp = datacomp['Texts'][j]   
    for i in range(len(data[1])):
        if list(data[1]['Input.slot1'])[i] == temp:
            conv_id[list(datacomp['Texts']).index((data[1]['Answer.change'][i]))]=conv_id[j]
            conv_id[list(datacomp['Texts']).index((data[1]['Answer.continuation'][i]))]=conv_id[j]
            conv_id[list(datacomp['Texts']).index((data[1]['Answer.elaboration'][i]))]=conv_id[j]
            conv_id[list(datacomp['Texts']).index((data[1]['Answer.joking_sarcastic'][i]))]=conv_id[j]
        
for i in range(len(data[1])*4):
    turn_id[i+len(data[0])*5]=2


temp1 = 0
for i in range(len(data[0])):
    indices = [j for j, x in enumerate(conv_id) if x == i]
    temp = turn_id[max(indices)]
    for k in range(len(indices)):
        temp1 = indices[k]
        no_turns[temp1] = temp

#print(no_turns)
header = ['Utterance_ID','Conversation_ID','No_Of_Turns','Turn_ID']
columns = []
columns.append(utt_id)
columns.append(conv_id)
columns.append(no_turns)
columns.append(turn_id)

with open('conversation.csv','w',newline='') as file:
    writer = csv.writer(file,delimiter=',')
    writer.writerows([header])
    writer.writerows(zip(*columns))
file.close()       
        
        
        
    
