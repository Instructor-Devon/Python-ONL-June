from django.db import models

# Create your models here.
class Player(models.Model):

    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    jersey_number = models.IntegerField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"