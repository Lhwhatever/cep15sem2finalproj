from django.contrib import admin
from . import models

# Register your models here.
admin.site.register(models.GameCategory)
admin.site.register(models.Location)
admin.site.register(models.Match)
admin.site.register(models.Tournament)
admin.site.register(models.PrivacySettings)
