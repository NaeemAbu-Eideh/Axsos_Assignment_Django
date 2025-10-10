from django.shortcuts import render, redirect
from . import models

from . import team_maker

def index(request):
	context = {
                'atlantic_soccor_conference_teams': models.all_teams_in_atlantic_league(),
                'players_in_boston_penguins': models.players_in_boston_penguins(),
	}
	return render(request, "leagues/index.html", context)

def make_data(request):
	team_maker.gen_leagues(10)
	team_maker.gen_teams(50)
	team_maker.gen_players(200)

	return redirect("index") 