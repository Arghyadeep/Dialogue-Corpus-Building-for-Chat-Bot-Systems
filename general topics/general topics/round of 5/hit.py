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
HIT_ID = [None]*len(datacomp)
HITTypeID = [None]*len(datacomp)

counter = 0
for i in range(len(data[0])):
    temp1 = data[0]['HITId'][i]
    temp2 = data[0]['HITTypeId'][i]
    for j in range(1,5):
        counter += 1
        if counter % 5 == 0:
            counter += 1
        HIT_ID[counter] = temp1
        HITTypeID[counter] = temp2
        
counter = 0
for i in range(len(data[1])):
    temp1 = data[1]['HITId'][i]
    temp2 = data[1]['HITTypeId'][i]

    for j in range(4):
        HIT_ID[len(data[0])*5 + counter]= temp1
        HITTypeID[len(data[0])*5 + counter] = temp2
        counter += 1
        
counter = 0
for i in range(len(data[2])):
    temp1 = data[2]['HITId'][i]
    temp2 = data[2]['HITTypeId'][i]

    for j in range(4):
        HIT_ID[len(data[0])*5 + len(data[1])*4 + counter]= temp1
        HITTypeID[len(data[0])*5 + len(data[1])*4 + counter] = temp2
        counter += 1
        
counter = 0
for i in range(len(data[3])):
    temp1 = data[3]['HITId'][i]
    temp2 = data[3]['HITTypeId'][i]

    for j in range(4):
        HIT_ID[len(data[0])*5 + len(data[1])*4 + len(data[2])*4 + counter]= temp1
        HITTypeID[len(data[0])*5 + len(data[1])*4 + len(data[2])*4 + counter] = temp2
        counter += 1
        
counter = 0
for i in range(len(data[4])):
    temp1 = data[4]['HITId'][i]
    temp2 = data[4]['HITTypeId'][i]

    for j in range(4):
        HIT_ID[len(data[0])*5 + len(data[1])*4 + len(data[2])*4 + len(data[3])*4 + counter]= temp1
        HITTypeID[len(data[0])*5 + len(data[1])*4 + len(data[2])*4 + len(data[3])*4 + counter] = temp2
        counter += 1

for i in range(len(datacomp)):
    if HIT_ID[i] == None:
        HIT_ID[i] = 'NA'
    if HITTypeID [i] == None:
        HITTypeID[i] = 'NA'
        
header = ['Utterance_ID','HITTypeID','HIT_ID']
columns = []
columns.append(utt_id)
columns.append(HITTypeID)
columns.append(HIT_ID)

with open('HIT.csv','w',newline='') as file:
    writer = csv.writer(file,delimiter=',')
    writer.writerows([header])
    writer.writerows(zip(*columns))
file.close()
