from django.shortcuts import render, redirect, HttpResponse
from datetime import datetime
from .models import Building

gold_map = {
    "temple": (10,20),
    "castle": (5,10),
    "shogun": (20,30),
}

SESSION_ACTIVITIES = "activities"

# Create your views here.
def index(request):
    # TODO: set up session for use in ninja gold game

    # check for session["gold"]
    if not "gold" in request.session:
        request.session["gold"] = 0
    # check for session["activities"]
    if not SESSION_ACTIVITIES in request.session:
        request.session[SESSION_ACTIVITIES] = []

    # Query for all buildings, pass as context object
    all_buildings = Building.objects.all()

    context = {
        "buildings": all_buildings,
        "newPlayer": "player" not in request.session # True if "player" in request.session False if not
    }
    return render(request, "home/index.html", context)

def player(request):
    player_name = request.POST["player"]
    request.session["player"] = player_name
    return redirect("/")

def gold(request):

    # query for building from request.POST["building_id"]
    
    # TODO: increment gold based on building type
    
    building = Building.objects.get(id=request.POST["building_id"])


    gold_this_turn = building.get_golds()

    # # check to see if we die
    # death_roll = random.randint(0,9)
    # if death_roll == 0 and building == "shogun":
    #     return redirect("/death")

    request.session["gold"] += gold_this_turn

    now = datetime.now()

    formatted_now = now.strftime("%Y/%m/%d %I:%M%p")

    # TODO: format message string for activity list
    message = f"You got {gold_this_turn} from {building.name} ({formatted_now})"

    messages = request.session[SESSION_ACTIVITIES]
    messages.append(message)
    request.session[SESSION_ACTIVITIES] = messages
    

    return redirect("/")

def death(request):
    return render(request, "home/youdie.html")