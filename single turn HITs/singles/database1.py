import pandas as pd
import csv


input_file = input("Enter input filename(with .csv extension): ")
output_file1 = input("Enter utterance file name: ")
output_file2 = input("Enter conversation file name: ")
output_file3 = input("Enter HIT file name: ")

data = pd.read_csv(input_file)
texts = []
dialogueacts = []
uniqueID = []

counter = -1
for i in range(len(data)*2):
    counter +=1
    uniqueID.append(counter)
    
    


for j in range(len(data)):
    texts.append(data['Input.slot0'][j])
    dialogueacts.append('prompt')
    texts.append(data['Answer.Your_Response'][j])
    dialogueacts.append('General Response')
    

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
for i in range(len(data)):
    counter +=1
    for j in range(2):
        conv_ID.append(counter)



HIT_ID = [None]*len(uniqueID)
HITTypeID = [None]*len(uniqueID)

counter = 0

hit = []
hittype = []

for i in range(len(data)):
    hit.append(data['HITId'][i])
    hittype.append(data['HITTypeId'][i])
      
for i in range(len(uniqueID)):
    if i%2 != 0:
        HIT_ID[i]=hit[int(i/2)]
        HITTypeID[i]=hittype[int(i/2)]
        

"""
counter = 0
for i in range(len(data)):
    for j in range(5):
        counter += 1
        if counter%5 != 0:
            HIT_ID[counter]=hit[i]
            HITTypeID[counter]=hittype[i]
"""
#print(HIT_ID)
#print(HITTypeID)

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

with open(output_file1,'w',newline='') as file:
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

with open(output_file2,'w',newline='') as file:
    writer = csv.writer(file,delimiter=',')
    writer.writerows([header2])
    writer.writerows(zip(*columns2))
file.close()

header3 = ['Utterance_ID','HITTypeID','HIT_ID']
columns3 = []
columns3.append(uniqueID)
columns3.append(HITTypeID)
columns3.append(HIT_ID)

with open(output_file3,'w',newline='') as file:
    writer = csv.writer(file,delimiter=',')
    writer.writerows([header3])
    writer.writerows(zip(*columns3))
file.close()
           


        
