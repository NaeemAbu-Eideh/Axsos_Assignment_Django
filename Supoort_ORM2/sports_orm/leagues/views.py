from django.shortcuts import render, redirect
from . import models

from . import team_maker

def index(request):
	context = {
                'atlantic_soccor_conference_teams': models.all_teams_in_atlantic_league(),
                'players_in_boston_penguins': models.players_in_boston_penguins(),
                'playesr_in_International_Collegiate_Baseball_Conference': models.all_playesr_in_International_Collegiate_Baseball_Conference(),
                'players__in_American_Conference_of_Amature_Football': models.get_players__in_American_Conference_of_Amature_Football(),
                'football_players': models.get_football_players(),
                'teams_contain_sophia_players': models.get_all_teams_contain_sophia_players(),
                'leagues_contain_sophia_players': models.get_all_leagues_contain_sophia_players(),
                'flores_does_not_currently_play_in_washington_roughriders': models.get_flores_does_not_currently_play_in_washington_roughriders(),
                'all_samuel_evans_teams': models.get_all_samuel_evans_teams(),
                'Manitoba_Tiger_Cats_all_players': models.get_Manitoba_Tiger_Cats_all_players(),
                'formerly_not_current_in_wichita_vikings': models.get_formerly_not_current_in_wichita_vikings(),
                'jacob_teams_without_current_team': models.get_jacob_teams_without_current_team(),
                'joshua_in_atlantic_federation_amature_besball_players': models.players_ever_play_in_atlantic_federation_amature_besball_players(),
                'had_12_or_more_players': models.get_teams_had_12_or_more_players(),
                'count_of_teams_for_each_player': models.get_count_of_teams_for_each_player()
	}
	return render(request, "leagues/index.html", context)

def make_data(request):
	team_maker.gen_leagues(10)
	team_maker.gen_teams(50)
	team_maker.gen_players(200)

	return redirect("index")