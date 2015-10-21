# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('onevone', '0006_auto_20151021_2329'),
    ]

    operations = [
        migrations.AlterField(
            model_name='match',
            name='participants',
            field=models.ManyToManyField(blank=True, to='acc.UserProfile', related_name='participated_matches'),
        ),
    ]
