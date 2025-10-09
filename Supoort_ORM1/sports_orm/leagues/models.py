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

"Dallas"

def get_all_basketball_leagues():
    return League.objects.filter(sport = "Baseball")


def get_all_women_leagues():
    return League.objects.filter(name__contains = "Womens'")

def get_all_leagues_with_any_hokey():
    return League.objects.filter(name__icontains = "hockey")

def get_all_without_football():
    return League.objects.exclude(sport = "Football")

def get_all_leagues_that_contain_conference():
    return League.objects.filter(name__icontains="Conference")

def get_all_leagues_in_atlantic_region():
    return League.objects.filter(name__startswith="Atlantic")

def get_teams_in_dallas():
    return Team.objects.filter(location = 'Dallas')

def get_teams_named_rabtors():
    return Team.objects.filter(team_name = "Raptors")

def get_all_city_locations():
    return Team.objects.filter(location__icontains = 'City')

def get_all_teams_that_bigin_with_t():
    return Team.objects.filter(team_name__startswith = 'T')

def all_teams_orderd_by_location():
    return Team.objects.all().order_by('location')

def all_teams_reverse_orderd_by_name():
    return Team.objects.all().order_by('-team_name')

def get_players_named_cooper():
    return Player.objects.filter(last_name = 'Cooper')

def get_players_named_joshua():
    return Player.objects.filter(first_name = 'Joshua')

def first_cooper_last_not_joshua():
    return Player.objects.filter(first_name = 'Cooper').exclude(last_name = "Joshua")

def first_alexander_wyatt():
    return Player.objects.filter(Q(first_name = 'Alexander') | Q(first_name = 'Wyatt'))