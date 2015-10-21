# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('acc', '0002_baseprivacysettings_messages'),
    ]

    operations = [
        migrations.CreateModel(
            name='GameCategory',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=63)),
                ('label', models.CharField(max_length=15)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=31)),
                ('full_text', models.TextField()),
                ('is_online', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Match',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('game', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('time_start', models.DateTimeField(verbose_name='Starting time')),
                ('time_end', models.DateTimeField(verbose_name='Ending time')),
                ('location', models.OneToOneField(to='onevone.Location')),
                ('owner', models.OneToOneField(to='acc.UserProfile', related_name='owned_matches')),
                ('participants', models.ForeignKey(to='acc.UserProfile', related_name='participated_matches')),
            ],
        ),
        migrations.CreateModel(
            name='PrivacySettings',
            fields=[
                ('baseprivacysettings_ptr', models.OneToOneField(to='acc.BasePrivacySettings', serialize=False, auto_created=True, primary_key=True, parent_link=True)),
                ('mode', models.IntegerField(verbose_name='Settings', choices=[(0, 'Completely private'), (1, 'Open for spectating'), (2, 'Open for participation')])),
                ('allow_regardless', models.ForeignKey(to='acc.UserProfile', related_name='allowed_for')),
                ('restrict_regardless', models.ForeignKey(to='acc.UserProfile', related_name='restricted_for')),
            ],
            bases=('acc.baseprivacysettings',),
        ),
        migrations.CreateModel(
            name='Tournament',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('time_start', models.DateTimeField(verbose_name='Starting time')),
                ('time_end', models.DateTimeField(verbose_name='Ending time')),
                ('location', models.OneToOneField(to='onevone.Location')),
                ('matches', models.ForeignKey(to='onevone.Match')),
                ('owner', models.OneToOneField(to='acc.UserProfile', related_name='owned_tourneys')),
                ('participants', models.ForeignKey(to='acc.UserProfile', related_name='participated_tourneys')),
                ('privacy', models.OneToOneField(to='onevone.PrivacySettings')),
            ],
        ),
        migrations.AddField(
            model_name='match',
            name='privacy',
            field=models.OneToOneField(to='onevone.PrivacySettings'),
        ),
        migrations.AddField(
            model_name='gamecategory',
            name='games',
            field=models.ForeignKey(to='onevone.Match', blank=True, null=True),
        ),
    ]
