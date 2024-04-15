from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from .chatbot import *
from django.http import JsonResponse
import pyrebase




config={
    "apiKey": "AIzaSyCu4F3cQUoT2o0oIBCKNTh10krTc3wfI_g",
    "authDomain": "ev-stations-66c6f.firebaseapp.com",
    "projectId": "ev-stations-66c6f",
    "databaseURL":"https://ev-stations-66c6f-default-rtdb.firebaseio.com/",
    "storageBucket": "ev-stations-66c6f.appspot.com",
    "messagingSenderId": "592696695132",
    "appId": "1:592696695132:web:e5cd5424cbf4d8d2584999",
    "measurementId": "G-9W1HMHH0NC"
}

firebase=pyrebase.initialize_app(config)
auth=firebase.auth()
database=firebase.database()
 



def index(request):
    print(database.child('data').child('test').get().val())

    return render(request, 'polls/index.html')

def about(request):
    return render(request, 'polls/about.html')
    

def map(request):
    return render(request, 'polls/map.html')
    

def pricing(request):
    return render(request, 'polls/pricing.html')


def station(request):
    if request.method=='POST':
        
        pass
    else:
        return render(request,"admin/station.html")

def addStation(request):
    return render(request,"admin/station.html")

def editStation(request):
    return render(request,"admin/station.html")

def deleteStation(request):
    return render(request,"admin/station.html")