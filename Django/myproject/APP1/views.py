# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from datetime import datetime
from django.shortcuts import render
from DownloadYoutubeAPI import detect as DYA
###### show view ######

def hello_world(request):
    template = 'hello_world.html'
    responds = {'current_time': str(datetime.now()),}
    return render(request,template,responds )

def Home(request):         
    template = 'showDB.html'
    responds = {'ALL_Post': ReadFromDB,}
    return render(request,template,responds)

def GetDataPage(request,Get_1,Get_2):         
    template = 'GetAndShow.html'
    responds = {'Get_1': str(Get_1.encode('utf-8')),'Get_2': str(Get_2),}
    return render(request,template,responds)

def YoutubeDownload(request,Url = 'znbKTbDGX1E'):
    Url_complete = 'https://www.youtube.com/watch?v='+str(Url.encode('utf-8'))
    template = 'YoutubeDownload.html'
    responds = {'SourceUrl': DYA(Url_complete),'current_time': str(datetime.now().strftime("%d/%m - %H%M%S")),'VideoID':Url}
    return render(request,template,responds)
###### show view END######


def Insert2DB(intitle,incontent,inlocation):
    DB_Main_list.objects.create(title=intitle, content=incontent, location=inlocation)

def ReadFromDB(pk=-1):
    '''
    input:     Post.objects.get(pk=1)
    output:    <Post: My First Trip>

    input:     Post.objects.filter(location__contains='台北')
    output:    [<Post: My First Trip>, <Post: Django 大冒險>]

    get：返回符合條件的唯一一筆資料。（注意：如果找不到符合條件的資料、或是有多筆資料符合條件，都會產生 exception）
    filter：返回符合條件的陣列。如果找不到任何資料則會返回空陣列。

    '''
    if pk != -1:
        return DB_Main_list.objects.get(pk=1)
    else:
        return DB_Main_list.objects.all()
    # print [p for p in Post.objects.all()]


