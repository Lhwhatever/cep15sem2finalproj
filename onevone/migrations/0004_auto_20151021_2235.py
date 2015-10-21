# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('onevone', '0003_auto_20151021_2233'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tournament',
            name='participants',
            field=models.ManyToManyField(blank=True, to='acc.UserProfile', related_name='participated_tourneys'),
        ),
    ]
