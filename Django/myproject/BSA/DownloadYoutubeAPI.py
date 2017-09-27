# coding:utf-8#
import json
import youtube_dl
import time
def detect(url):
    '''
        How to Using:
            detect('youtube video link')
        How to show Data:
            for r in DownloadLinkList:
                print(r['info'])
                print(r['url'])
    '''
    try:
        ydl = youtube_dl.YoutubeDL({'outtmpl': '%(id)s%(ext)s'})
        
        with ydl:
            result = ydl.extract_info(url,download=False)
    
        if 'entries' in result:
            # Can be a playlist or a list of videos
            video = result['entries'][0]
        else:
            # Just a video
            video = result
        
        #print(video)
        video_url = video['formats']
        video_url = len(video['formats'])
        #video_url = video['formats'][0]['url']
        
        SourceArray=[]
        for key in video['formats']:
            #print(key['format'])
            #print(key['url'])
            #print('\n\n\n\n\n\n')
            SourceArray.append({'info':key['format'],'url':key['url']})
        
        row_json = json.dumps(SourceArray)
        
        #print row_json
        
        return SourceArray
    except:
        return [{"info":"網址錯誤","url":"#"}]



