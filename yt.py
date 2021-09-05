import youtube_dl
url=input(str("enter url :",))
ydl={}
with youtube_dl.YoutubeDL(ydl)as Ydl:
    Ydl.download([url])