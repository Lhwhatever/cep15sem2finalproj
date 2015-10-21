# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('acc', '0003_auto_20151021_2232'),
        ('onevone', '0002_auto_20151021_2231'),
    ]

    operations = [
        migrations.AddField(
            model_name='match',
            name='vacancies',
            field=models.IntegerField(default=5),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='match',
            name='owner',
            field=models.ForeignKey(related_name='owned_matches', to='acc.UserProfile'),
        ),
        migrations.RemoveField(
            model_name='match',
            name='participants',
        ),
        migrations.AddField(
            model_name='match',
            name='participants',
            field=models.ManyToManyField(related_name='participated_matches', to='acc.UserProfile'),
        ),
        migrations.AlterField(
            model_name='tournament',
            name='owner',
            field=models.ForeignKey(related_name='owned_tourneys', to='acc.UserProfile'),
        ),
        migrations.RemoveField(
            model_name='tournament',
            name='participants',
        ),
        migrations.AddField(
            model_name='tournament',
            name='participants',
            field=models.ManyToManyField(related_name='participated_tourneys', to='acc.UserProfile'),
        ),
    ]
