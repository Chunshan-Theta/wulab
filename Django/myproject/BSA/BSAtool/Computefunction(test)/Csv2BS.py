#coding:utf-8
#Csv file of Source Data convert to Behavior Sequential 
'''
using :
Set var:
    CsvDir ='DataFormWuret.csv'     #Data from and name 
    listtitle = 'group_argu_code'   #Row name 
    TypeNum = 6                     #Number of motion type
    SelectedGroup = '21'            #Name of Selected Group
Read file:
    SourceData = ReadFile(CsvDir)
Compute Motion array:
    ComputeMotionIndex(SourceData,TypeNum,'21')
'''
import csv
import numpy



def ComputeMotionIndex(listmotion,TypeNum,wantSet='-1'):
    FirstMotion = -1
    SecondMotion = -1    
     
    TypeNum +=1 # Because Data not contain 0
    MotionSet=numpy.zeros((TypeNum,TypeNum),int)
    for index in range(TypeNum-1):
        MotionSet[0][index+1]=index+1
        MotionSet[index+1][0]=index+1

    for index in range(len(listmotion)-1):
        if listmotion[index][0] == listmotion[index+1][0] and (wantSet == listmotion[index][0] or wantSet == '-1'):
            # if not same group, pass
            # if didn't select group, pass
            FirstMotion = listmotion[index][1]
            SecondMotion = listmotion[index+1][1]
            MotionSet[FirstMotion][SecondMotion] += 1
    print MotionSet

def ReadFile(FileDir):
    listmotion = []
    Tfile = open(FileDir, 'r')
    csvCursor = csv.reader(Tfile)
    for row in csvCursor:
        if row[2] != '' and row[2] !=listtitle:
            listmotion.append([str(row[0]),int(row[2])])# Group , type
    Tfile.close()
    return listmotion





CsvDir ='DataFormWuret.csv' 
listtitle = 'group_argu_code'
TypeNum = 6
SelectedGroup = '21'
ComputeMotionIndex(ReadFile(CsvDir),TypeNum,SelectedGroup)
