from django.db import models
from django.db.models import Q
class League(models.Model):
	name = models.CharField(max_length=50)
	sport = models.CharField(max_length=15)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

class Team(models.Model):
	location = models.CharField(max_length=50)
	team_name = models.CharField(max_length=50)
	league = models.ForeignKey(League, related_name="teams", on_delete = models.CASCADE)

class Player(models.Model):
	first_name = models.CharField(max_length=15)
	last_name = models.CharField(max_length=15)
	curr_team = models.ForeignKey(Team, related_name="curr_players", on_delete = models.CASCADE)
	all_teams = models.ManyToManyField(Team, related_name="all_players") 

def all_teams_in_atlantic_league():
    league = League.objects.filter(name="Atlantic Soccer Conference")
    if(len(league) == 0):
        return []
    return league.teams.all()

def players_in_boston_penguins():
    team = Team.objects.filter(team_name = "Penguins", location = "Boston")
    if(len(team) == 0):
        return []
    players = team.all_players.all()
    if(len(players) == 0):
        return []
    return players