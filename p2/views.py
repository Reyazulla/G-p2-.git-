from django.http import HttpResponse
from  django.shortcuts import render

def index(request):
    return HttpResponse("hello world")
def home(request):
    return HttpResponse("wellcone to n")
def html_demo3(request):
    return render(request,"sample1.html")


