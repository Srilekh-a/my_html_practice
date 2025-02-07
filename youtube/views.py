from django.shortcuts import render , redirect
from pytube import *
# Create your views here.
def youtube(request):
    if request.method=='POST':
        link=request.POST['link']
        video =youtube(link)
        stream = video.streams.get_lowest_reaolution()
        stream.download()
        return render(request,'youtube1.html')
    return render(request,'youtube1.html')
