from django.db import models


# Create your models here.
import acc


class Location(models.Model):
    app_label = 'onevone'
    name = models.CharField(max_length=31)
    full_text = models.TextField()
    is_online = models.BooleanField()
    
    
class PrivacySettings(acc.models.BasePrivacySettings):
    app_label = 'onevone'
    SETTINGS = (
        (0, 'Completely private'),
        (1, 'Open for spectating'),
        (2, 'Open for participation')
    )

    allow_regardless = models.ForeignKey(acc.models.UserProfile, related_name="allowed_for")
    restrict_regardless = models.ForeignKey(acc.models.UserProfile, related_name="restricted_for")

    mode = models.IntegerField(verbose_name='Settings', choices=SETTINGS)
    
    
class Match(models.Model):
    app_label = 'onevone'
    name = models.CharField(max_length=255)
    description = models.TextField()

    owner = models.OneToOneField(acc.models.UserProfile, related_name="owned_matches")
    participants = models.ForeignKey(acc.models.UserProfile, related_name="participated_matches")

    location = models.OneToOneField(Location)
    time_start = models.DateTimeField(verbose_name="Starting time")
    time_end = models.DateTimeField(verbose_name="Ending time")

    privacy = models.OneToOneField(PrivacySettings)
    
    
class GameCategory(models.Model):
    app_label = 'onevone'
    name = models.CharField(max_length=31)
    description = models.TextField()

    games = models.ForeignKey(Match)

    def __str__(self):
        return self.name


class Tournament(models.Model):
    app_label = 'onevone'
    name = models.CharField(max_length=255)
    description = models.TextField()

    owner = models.OneToOneField(acc.models.UserProfile, related_name="owned_tourneys")
    participants = models.ForeignKey(acc.models.UserProfile, related_name="participated_tourneys")

    location = models.OneToOneField(Location)
    time_start = models.DateTimeField(verbose_name="Starting time")
    time_end = models.DateTimeField(verbose_name="Ending time")

    matches = models.ForeignKey(Match)

    privacy = models.OneToOneField(PrivacySettings)
