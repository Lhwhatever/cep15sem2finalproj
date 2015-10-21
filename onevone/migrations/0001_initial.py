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
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('name', models.CharField(max_length=31)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('name', models.CharField(max_length=31)),
                ('full_text', models.TextField()),
                ('is_online', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Match',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('time_start', models.DateTimeField(verbose_name='Starting time')),
                ('time_end', models.DateTimeField(verbose_name='Ending time')),
                ('location', models.OneToOneField(to='onevone.Location')),
                ('owner', models.OneToOneField(related_name='owned_matches', to='acc.UserProfile')),
                ('participants', models.ForeignKey(related_name='participated_matches', to='acc.UserProfile')),
            ],
        ),
        migrations.CreateModel(
            name='PrivacySettings',
            fields=[
                ('baseprivacysettings_ptr', models.OneToOneField(primary_key=True, serialize=False, parent_link=True, to='acc.BasePrivacySettings', auto_created=True)),
                ('mode', models.IntegerField(verbose_name='Settings', choices=[(0, 'Completely private'), (1, 'Open for spectating'), (2, 'Open for participation')])),
                ('allow_regardless', models.ForeignKey(related_name='allowed_for', to='acc.UserProfile')),
                ('restrict_regardless', models.ForeignKey(related_name='restricted_for', to='acc.UserProfile')),
            ],
            bases=('acc.baseprivacysettings',),
        ),
        migrations.CreateModel(
            name='Tournament',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('time_start', models.DateTimeField(verbose_name='Starting time')),
                ('time_end', models.DateTimeField(verbose_name='Ending time')),
                ('location', models.OneToOneField(to='onevone.Location')),
                ('matches', models.ForeignKey(to='onevone.Match')),
                ('owner', models.OneToOneField(related_name='owned_tourneys', to='acc.UserProfile')),
                ('participants', models.ForeignKey(related_name='participated_tourneys', to='acc.UserProfile')),
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
            field=models.ForeignKey(to='onevone.Match'),
        ),
    ]
