from django.shortcuts import render
from django.http import HttpResponse
#import data from database to display on webpage
from p1.models import Info
# Create your views 
def index(request):
    movieobjects=Info.objects.all()
    context={'movieobjects':movieobjects}
    return render(request,'index.html',context)
    
