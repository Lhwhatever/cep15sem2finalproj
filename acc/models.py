from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(User)

    website = models.URLField(blank=True)
    status = models.TextField(blank=True)

    def __str__(self):
        return self.user.username

    @classmethod
    def get(cls, user):
<<<<<<< HEAD
        return cls.objects.get(user=user) if user.is_authenticated() else None
=======
        return cls.objects.all.get(user=user) if user.is_authenticated() else None


class BasePrivacySettings(models.Model):
    owner = models.OneToOneField(User)
    settings = models.CharField(max_length=2, choices=())
>>>>>>> 93d751b32678b643dc2bf2f0d473c6618a2dd0ef
