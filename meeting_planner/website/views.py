from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime


# Create your views here.

def welcome(request):
    return HttpResponse("Welcome to the Meeting Planer!")

def date(request):
    return HttpResponse("This page was served at " + str(datetime.now()))

#About page
def about(request):
    return HttpResponse("I'm Luong and I lead the back-end engineer team!")