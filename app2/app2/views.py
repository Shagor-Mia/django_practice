from django.http import HttpResponse
from django.shortcuts import render

def HomePage(request):
     return render(request,"index.html")
  
def aboutUs(request):
    return HttpResponse('welcome to myside')

def course(request):
    return HttpResponse('<b>we are providing best course.</b>')

def courseDetails(request,courseid):
    return HttpResponse(courseid)