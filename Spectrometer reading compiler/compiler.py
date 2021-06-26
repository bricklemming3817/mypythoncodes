import pandas as pd
import re
import time
from tqdm import tqdm
print('Welcome to Vernier Scale Reading Compiler!')
time.sleep(2)

while True:
    excelsheet = input("Enter name of excel sheet: ")
    data = pd.read_excel(excelsheet)
    data.dropna(axis=1, inplace=True)
    time.sleep(2)
    print('\nExcel Sheet successfully Loaded!')
    leastcount = int(input("Enter the value of Least Count(in seconds): "))

    MSR = data['MSR']
    VSD = data['VSD']
    TR = []

    for j, i in tqdm(enumerate(MSR)):
        if re.search("\°(.*?)\'", i) == None:
            i = str(i) + str(0) + "'"
        MSR[j] = i

    for j, i in tqdm(enumerate(MSR)):
        if re.search('\'(.*?)\"', i) == None:
            i = str(i) + str(0) + '"'
        MSR[j] = i
    data['MSR'] = MSR

    if len(MSR) != len(VSD):
        print("ERROR: MISSING VALUES DETECTED")

    VSR = VSD * leastcount
    for j, i in enumerate(VSR):
        m, s = divmod(i, 60)
        msd = str(0) + '°' + str(m) + "'" + str(s) + '"'
        VSR[j] = msd
    VSR = list(VSR)
    data['VSR'] = VSR

    for i, j in zip(MSR, VSR):
        degrees1 = float(i.split('°')[0])
        degrees2 = float(j.split('°')[0])
        degrees = degrees1 + degrees2

        minutes1 = float(re.search("\°(.*?)\'", i)[0][1:-1])
        minutes2 = float(re.search("\°(.*?)\'", j)[0][1:-1])
        minutes = minutes1 + minutes2

        seconds1 = float(re.search('\'(.*?)\"', i)[0][1:-1])
        seconds2 = float(re.search('\'(.*?)\"', j)[0][1:-1])
        seconds = seconds1 + seconds2

        seconds = divmod(seconds, 60)[1]
        minutes += divmod(seconds, 60)[0]
        minutes = divmod(minutes, 60)[1]
        degrees += divmod(minutes, 60)[0]

        tr = str(int(degrees)) + '°' + str(int(minutes)) + "'" + str(int(seconds)) + '"'
        TR.append(tr)

    data['TR'] = TR

    filename = excelsheet.split('.')[0] + '_result.xlsx'
    data.to_excel(filename)

    print('\nOperation has been successfully completed! Result has been save as ', filename, 'in the same directory')

    print('\nsend feedbacks to bricklemming3817@gmail.com')
    x = input("press 'x' and 'return' to close, press 'y' to run the programme again ")
    if x == 'x':
        break
    else:
        pass




