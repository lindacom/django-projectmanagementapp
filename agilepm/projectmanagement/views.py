from django.http import HttpResponse
from django.shortcuts import render
from .models import Video, Article

# Create your views here.
# returning the app name in the templates folder / and then the template html file

def index (request):
    return render (request, 'projectmanagement/index.html')

def projectmanagement (request):
    return render (request, 'projectmanagement/projectmanagement.html')

def projectactivities (request):
    return render (request, 'projectmanagement/projectactivities.html')

def agileprojectmanagement (request):
    return render (request, 'projectmanagement/agileprojectmanagement.html')

def resources (request):
    videos = Video.objects.all()
    articles = Article.objects.all()
    return render(request, 'projectmanagement/resources.html', context={'videos':videos, 'articles':articles})
