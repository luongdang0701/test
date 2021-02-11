from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from django.template import loader


# Create your views here.

def welcome(request):
    return render(request, 'index.html',{})

def date(request):
    return HttpResponse("This page was served at " + str(datetime.now()))

#About page
def about(request):
    return HttpResponse("I'm Luong and I lead the back-end engineer team!")

def vishakha(request):
    return render(request, 'vishakha.html',{})



def rebecca(request):
    return render(request, 'rebecca.html',{})

def luong(request):
    return render(request, 'luong.html',{})

def bryan(request):
    return render(request, 'bryan.html',{})

def ashwini(request):
    return render(request, 'ashwini.html',{})

def malcolm(request):
    return render(request, 'malcolm.html',{})
