from django.db import models
from django.db.models import Q, Count
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
    team_id = team.values_list('id', flat = True)
    players = Player.objects.filter(curr_team__in = team_id)
    return players

def all_playesr_in_International_Collegiate_Baseball_Conference():
    leagues = League.objects.filter(name = 'International Collegiate Baseball Conference')
    leagues_id = leagues.values_list('id', flat = True)
    teams = Team.objects.filter(league__in = leagues_id)
    teams_id = teams.values_list('id', flat=True)
    players = Player.objects.filter(curr_team__in = teams_id)
    return players

def get_players__in_American_Conference_of_Amature_Football():
    leagues = League.objects.filter(name__contains = "American", sport = "Football")
    leagues_id = leagues.values_list('id', flat = True)
    teams = Team.objects.filter(league__in = leagues_id)
    teams_id = teams.values_list('id', flat=True)
    players = Player.objects.filter(curr_team__in = teams_id, last_name = 'Lopez')
    return players

def get_football_players():
    leagues = League.objects.filter(sport = 'Football')
    leagues_id = leagues.values_list('id', flat=True)
    all_teams = Team.objects.filter(league__in= leagues_id)
    all_teams_id = all_teams.values_list('id', flat=True)
    all_players = Player.objects.filter(all_teams__in = all_teams_id)
    return all_players


def get_all_teams_contain_sophia_players():
    players = Player.objects.filter(first_name = "Sophia")
    players_id = players.values_list('id', flat=True)
    teams = Team.objects.filter(curr_players__in = players_id)
    return teams

def get_all_leagues_contain_sophia_players():
    players = Player.objects.filter(first_name = "Sophia")
    players_id = players.values_list('id', flat=True)
    teams = Team.objects.filter(curr_players__in = players_id)
    teams_id = teams.values_list('id', flat=True)
    leagues = League.objects.filter(teams__in = teams_id)
    return leagues

def get_flores_does_not_currently_play_in_washington_roughriders():
    team = Team.objects.filter(location = 'Washington', team_name = 'Roughriders')
    team_id = team.values_list('id', flat = True)
    players = Player.objects.filter(last_name = 'Flores').exclude(curr_team__in = team_id)
    return players

def get_all_samuel_evans_teams():
    player = Player.objects.filter(first_name = 'Samuel', last_name = 'Evans')
    player_id = player.values_list('id', flat= True)
    teams = Team.objects.filter(all_players__in = player_id)
    return teams

def get_Manitoba_Tiger_Cats_all_players():
    team = Team.objects.filter(location = 'Manitoba', team_name = 'Tiger-Cats')
    team_id = team.values_list('id', flat=True)
    players = Player.objects.filter(all_teams__in = team_id)
    return players

def get_formerly_not_current_in_wichita_vikings():
    team = Team.objects.filter(location = 'Wichita', team_name = 'Vikings')
    team_id = team.values_list('id', flat = True)
    players = Player.objects.filter(all_teams__in = team_id).exclude(curr_team__in = team_id)
    return players

def get_jacob_teams_without_current_team():
    player = Player.objects.filter(first_name = 'Jacob', last_name = 'Gray')
    player_id = player.values_list('id', flat=True)
    teams = Team.objects.filter(all_players__in = player_id).exclude(curr_players__in = player_id)
    return teams

def players_ever_play_in_atlantic_federation_amature_besball_players():
    league = League.objects.filter(name = 'Atlantic Federation Amateur Players', sport = 'Baseball')
    league_id = league.values_list('id', flat = True)
    teams = Team.objects.filter(league__in = league_id)
    teams_id = teams.values_list('id', flat = True)
    players = Player.objects.filter(first_name = 'Joshua', all_teams__in = teams_id)
    return players

def get_teams_had_12_or_more_players():
    teams = Team.objects.annotate(number_of_players = Count('all_players', distinct=True)).filter(number_of_players__gte = 12)
    return teams

def get_count_of_teams_for_each_player():
    players = Player.objects.annotate(num_teams = Count('all_teams', distinct=True)).order_by('num_teams')
    return players