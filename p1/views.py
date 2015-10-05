from django.shortcuts import render
from django.http import HttpResponse
import os
import re
#import data from database to display on webpage
from p1.models import Info
# Create your views 
def index(request):
    #handles FORM POST REQUESTS
    if(request.POST):
        # Extract the youtube ID from the url source freshtomatos.py from udacity
        youtube_id_match = re.search(
            r'(?<=v=)[^&#]+', request.POST["youtubeurl"])
        youtube_id_match = youtube_id_match or re.search(
            r'(?<=be/)[^&#]+', request.POST["youtubeurl"])
        trailer_youtube_id = (youtube_id_match.group(0) if youtube_id_match
                              else None)
        new_movie=Info(title=request.POST["title"],link=trailer_youtube_id,imgurl=request.POST["imgurl"])
        new_movie.save()
        movieobjects=Info.objects.all()
        context={'movieobjects':movieobjects}
        return render(request,'index.html',context)
    movieobjects=Info.objects.all()
    context={'movieobjects':movieobjects}
    return render(request,'index.html',context)
    
