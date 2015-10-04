from django.shortcuts import render
from django.http import HttpResponse
#import data from database to display on webpage
from p1.models import Info
# Create your views 
def index(request):
    #handles FORM POST REQUESTS
    if(request.POST):
        new_movie=Info(title=request.POST["title"],link=request.POST["youtubeurl"],imgurl=request.POST["imgurl"])
        new_movie.save()
        movieobjects=Info.objects.all()
        context={'movieobjects':movieobjects}
        return render(request,'index.html',context)
    movieobjects=Info.objects.all()
    context={'movieobjects':movieobjects}
    return render(request,'index.html',context)
    
