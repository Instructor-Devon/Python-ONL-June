from django.db import models
from datetime import datetime

class PartyPersonManager(models.Manager):
    def validate(self, form_stuff):
        errors = []
        if form_stuff['name'] == "":
            errors.append("Name field is required")
        # validate birthday!
        # form_stuff['birthday'] => '2019-07-01'
        diff = datetime.now() - datetime.strptime(form_stuff["birthday"], "%Y-%m-%d")
        if diff.days/365 < 21:
            errors.append("must be 21 or over to party")
        return errors

# Create your models here.
class PartyPerson(models.Model):
    name = models.CharField(max_length=45)
    # TODO: validate birthday 21 and over
    birthday = models.DateField()
    # one to many PartyPerson => Party
    # parties_planned
    objects = PartyPersonManager()

class Party(models.Model):
    name = models.CharField(max_length=45)
    location = models.CharField(max_length=45)
    # one to many PartyPerson => Party
    host = models.ForeignKey(PartyPerson, related_name="parties_planned")