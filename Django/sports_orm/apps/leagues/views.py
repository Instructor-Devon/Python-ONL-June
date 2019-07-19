from django.shortcuts import render, redirect
from .models import League, Team, Player

from . import team_maker

def index(request):

	# Find all baseball leagues
	baseball_leagues = League.objects.filter(sport="Baseball")
	# Find all womens' leagues
	# League.objects.filter(name__contains="Women")

	# Find all leagues where sport is any type of hockey
	# League.objects.filter(sport__contains="Hockey")

	# Find all leagues where sport is something OTHER THAN football
	# League.objects.exclude(sport="Football")

	# Find all teams, past and present, that Samuel Evans has played with
	# Team.objects.filter(Q(all_players__id=115) | Q(curr_players__id=115)).distinct()
	

	context = {
		"leagues": League.objects.all(),
		"teams": Team.objects.all(),
		"players": Player.objects.all(),
	}
	return render(request, "leagues/index.html", context)

def make_data(request):
	team_maker.gen_leagues(10)
	team_maker.gen_teams(50)
	team_maker.gen_players(200)

	return redirect("index")