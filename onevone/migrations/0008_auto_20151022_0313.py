# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('onevone', '0007_auto_20151021_2354'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tournament',
            name='matches',
        ),
        migrations.AddField(
            model_name='match',
            name='tourney',
            field=models.ForeignKey(blank=True, to='onevone.Tournament', null=True),
        ),
        migrations.AddField(
            model_name='tournament',
            name='category',
            field=models.ForeignKey(to='onevone.GameCategory', default=None),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='tournament',
            name='game',
            field=models.CharField(max_length=255, default='Club Penguin'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='tournament',
            name='vacancies',
            field=models.IntegerField(default=5),
            preserve_default=False,
        ),
    ]
