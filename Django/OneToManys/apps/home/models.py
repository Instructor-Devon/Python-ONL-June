from django.db import models

# Create your models here.
class Team(models.Model):
    # id
    city = models.CharField(max_length=45)
    team_name = models.CharField(max_length=45)

    # players
    # ie. someTeam.players.all() => [player, player, player]

class Player(models.Model):
    # id
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)

    # team_id
    team = models.ForeignKey(Team, related_name="players")
    # ie. somePlayer.team.city