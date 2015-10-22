from django.db import models
import hashlib
import base64


# Create your models here.
import acc

PRIVACY_SETTINGS = (
        (0, 'Completely private'),
        (1, 'Open for spectating'),
        (2, 'Open for participation')
)


class Location(models.Model):
    app_label = 'onevone'
    name = models.CharField(max_length=31)
    full_text = models.TextField()
    is_online = models.BooleanField()
    
    def __str__(self):
        return "{0!s}{1}".format(self.name, " (online)" if self.is_online else "")
    

class GameCategory(models.Model):
    app_label = 'onevone'
    name = models.CharField(max_length=63)
    label = models.CharField(max_length=15)
    description = models.TextField()

    def __str__(self):
        return self.name
        

class Tournament(models.Model):
    app_label = 'onevone'
    name = models.CharField(max_length=255)
    game = models.CharField(max_length=255)
    description = models.TextField()

    category = models.ForeignKey(GameCategory)

    owner = models.ForeignKey(acc.models.UserProfile, related_name="owned_tourneys")
    participants = models.ManyToManyField(acc.models.UserProfile, related_name="participated_tourneys", blank=True)
    vacancies = models.IntegerField()

    location = models.OneToOneField(Location)
    time_start = models.DateTimeField(verbose_name="Starting time")
    time_end = models.DateTimeField(verbose_name="Ending time")

    privacy = models.IntegerField(verbose_name="Privacy settings", choices=PRIVACY_SETTINGS)

    @property
    def privacy_settings(self):
        return [item for item in PRIVACY_SETTINGS if item[0] == self.privacy][0][1]
        
    def __str__(self):
        return self.name
        
        
class Match(models.Model):
    app_label = 'onevone'

    name = models.CharField(max_length=255)
    game = models.CharField(max_length=255)
    description = models.TextField()
    
    category = models.ForeignKey(GameCategory)

    owner = models.ForeignKey(acc.models.UserProfile, related_name="owned_matches")
    participants = models.ManyToManyField(acc.models.UserProfile, related_name="participated_matches", blank=True)
    
    vacancies = models.IntegerField()

    location = models.OneToOneField(Location)
    time_start = models.DateTimeField(verbose_name="Starting time")
    time_end = models.DateTimeField(verbose_name="Ending time")

    privacy = models.IntegerField(verbose_name="Privacy settings", choices=PRIVACY_SETTINGS)

    tourney = models.ForeignKey(Tournament, blank=True, null=True)
    
    def __str__(self):
        return "{0!s}'s {1!s}".format(self.owner, self.name)
        
    @property
    def privacy_settings(self):
        return [item for item in PRIVACY_SETTINGS if item[0] == self.privacy][0][1]
