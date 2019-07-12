from django.db import models
import random

# Create your models here.
class Building(models.Model):
    name = models.CharField(max_length=45)
    min_gold = models.IntegerField()
    max_gold = models.IntegerField()

    def get_golds(self):
        return random.randint(self.min_gold, self.max_gold)

    def __str__(self):
        return self.name