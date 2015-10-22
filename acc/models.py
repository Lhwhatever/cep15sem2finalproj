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
        return cls.objects.get(user=user) if user.is_authenticated() else None
    
    
class Messages(models.Model):
    subject = models.CharField(max_length=255)
    content = models.TextField()
    
    sender = models.ForeignKey(UserProfile, related_name='sended')
    recipient = models.ForeignKey(UserProfile, related_name='received')

    sent = models.DateTimeField(verbose_name="Time sent", auto_now=True)
    
    def __str__(self):
        return "Message at {0!s}".format(self.sent)
