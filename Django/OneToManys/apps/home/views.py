from django.shortcuts import render, redirect
from .models import Player, Team
# Create your views here.
def index(request):
    context = {
        "players": Player.objects.all(),
        "teams": Team.objects.all()
    }
    return render(request, "home/index.html", context)
def create_player(request):
    # create player in database
    # go grab a team with id = request.POST["team"]
    theTeam = Team.objects.get(id=request.POST["team"])
    Player.objects.create(first_name = request.POST["first_name"], last_name = request.POST["last_name"], team=theTeam)
    return redirect("/")

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