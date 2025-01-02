from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
# returning the app name in the templates folder / and then the template html file

def projectmanagement (request):
    return render (request, 'projectmanagement/projectmanagement.html')

def projectactivities (request):
    return render (request, 'projectmanagement/projectactivities.html')
