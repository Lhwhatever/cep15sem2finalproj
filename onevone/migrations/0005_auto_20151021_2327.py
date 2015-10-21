# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('onevone', '0004_auto_20151021_2235'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='gamecategory',
            name='games',
        ),
        migrations.AddField(
            model_name='match',
            name='category',
            field=models.ForeignKey(null=True, to='onevone.GameCategory'),
        ),
    ]
