# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from datetime import datetime
from django.shortcuts import render
from BSAClass import BSA
###### show view ######

def hello_world(request):
    template = 'hello_world.html'
    responds = {'current_time': str(datetime.now()),}
    return render(request,template,responds )

def Cal_BSA(request):
    try:
        input_text = request.POST['content']#linebreaks
        NumOfBS = int(request.POST['NumOfBS'])
        Group = int(request.POST['Group'])
        content = "\n".join(input_text.splitlines())
        #print content
    except Exception as e:
        print e
        print "error!! Can NOT catch POST['content']"
        content = "empty"
        input_text = "empty"
        NumOfBS = 6
        Group= -1
    if content != "empty":
        try:
            if Group != -1:
                print Group
                TheBSA = BSA(content,NumOfBS)
                TheBSA.ComputeMotionGroup(int(Group))
                content = TheBSA.show(2)
            else:
                content = BSA(content,NumOfBS).show(2)
        except Exception as e:
            print "Error when convert to BSA ",e

    
    template = 'CalBSA.html'
    responds = {'current_time': str(datetime.now()),
        'csv_data': input_text,
        'array_BSA': content,
        'NumOfBS':NumOfBS,
        'Group':Group
                }
    return render(request,template,responds )

def Home(request):         
    template = 'showDB.html'
    responds = {'ALL_Post': ReadFromDB,}
    return render(request,template,responds)

def GetDataPage(request,Get_1,Get_2):         
    template = 'GetAndShow.html'
    responds = {'Get_1': str(Get_1.encode('utf-8')),'Get_2': str(Get_2),}
    return render(request,template,responds)


###### show view END######




