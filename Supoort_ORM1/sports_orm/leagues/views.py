from django.shortcuts import render, redirect
from . import models

from . import team_maker

def index(request):
	context = {
        "baseball": models.get_all_basketball_leagues(),
        "women": models.get_all_women_leagues(),
        'hockies': models.get_all_leagues_with_any_hokey(),
        'all_without_football': models.get_all_without_football(),
        'leagues_with_conference': models.get_all_leagues_that_contain_conference(),
        'atlantic_region': models.get_all_leagues_in_atlantic_region(),
        'dallas': models.get_teams_in_dallas(),
        'raptors': models.get_teams_named_rabtors(),
        'city_location': models.get_all_city_locations(),
        'begin_with_t': models.get_all_teams_that_bigin_with_t(),
        'all_teams_orderd_by_location': models.all_teams_orderd_by_location(),
        'all_teams_reverse_orderd_by_name': models.all_teams_reverse_orderd_by_name(),
        'named_cooper': models.get_players_named_cooper(),
        'named_joshua': models.get_players_named_joshua(),
        'first_cooper_last_not_joshua': models.first_cooper_last_not_joshua(),
        'first_alexander_wyatt': models.first_alexander_wyatt()
        
	}
	return render(request, "leagues/index.html", context)

def make_data(request):
	team_maker.gen_leagues(10)
	team_maker.gen_teams(50)
	team_maker.gen_players(200)

	return redirect("index")