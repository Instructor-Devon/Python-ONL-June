from django.shortcuts import render, HttpResponse, render
import requests

# Create your views here
def index(request):
    r = requests.get("http://www.dnd5eapi.co/api/classes/")
    
    context = {
        "user": {
            "username": "Xx_dev_hacker_xX",
            "id": 3,
        },
        "classes": r.json()["results"],
        "numbers": [32,356,56,243],
    }
    return render(request, "home/index.html", context)

def other(request):
    return HttpResponse("Other function here!")

def show(request, user_id):
    return HttpResponse(f"Hello user #{user_id}")