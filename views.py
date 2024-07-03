from django.http import HttpResponse
from django.shortcuts import render
from .myfile import eventform
def index(request):
    return render(request, 'index.html')
    #return HttpResponse("Hello")
def add(request):
    return HttpResponse("Enter event details")
def display(request):
    return HttpResponse("display event details")
def Update(request):
    return HttpResponse("Update event details")