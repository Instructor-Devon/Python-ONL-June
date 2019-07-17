from django.shortcuts import render, redirect
from django.contrib.messages import error
from .models import Player, Team
# Create your views here.
def index(request):
    context = {
        "players": Player.objects.all(),
        "teams": Team.objects.all()
    }
    error(request, "Invalid stuff lol")
    error(request, "Do it better silly")

    return render(request, "home/index.html", context)
def create_player(request):
    # create player in database
    # go grab a team with id = request.POST["team"]
    theTeam = Team.objects.get(id=request.POST["team"])
    newPlayer = Player.objects.create(first_name = request.POST["first_name"], last_name = request.POST["last_name"], team=theTeam)
    # newPlayer.id is something we can redirect to!
    return redirect(f"/players/{newPlayer.id}")

def player(request, player_id):
    # query for player with id
    p = Player.objects.get(id=player_id)
    context = {
        "player": p
    }
    return render(request, "home/player.html", context)

def team(request, team_id):
    # query for player with id
    t = Team.objects.get(id=team_id)
    context = {
        "team": t
    }
    return render(request, "home/team.html", context)

def cities(request, city_name):
    teams_in_city = Team.objects.filter(city=city_name)
    players_in_city = Player.objects.filter(team__city=city_name)
    context = {
        "teams": teams_in_city,
        "players": players_in_city,
        "city": city_name
    }
    return render(request, "home/city.html", context)
