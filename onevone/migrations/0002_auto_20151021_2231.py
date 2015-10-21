# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('onevone', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='privacysettings',
            name='allow_regardless',
        ),
        migrations.RemoveField(
            model_name='privacysettings',
            name='baseprivacysettings_ptr',
        ),
        migrations.RemoveField(
            model_name='privacysettings',
            name='restrict_regardless',
        ),
        migrations.AlterField(
            model_name='match',
            name='privacy',
            field=models.IntegerField(choices=[(0, 'Completely private'), (1, 'Open for spectating'), (2, 'Open for participation')], verbose_name='Privacy settings'),
        ),
        migrations.AlterField(
            model_name='tournament',
            name='privacy',
            field=models.IntegerField(choices=[(0, 'Completely private'), (1, 'Open for spectating'), (2, 'Open for participation')], verbose_name='Privacy settings'),
        ),
        migrations.DeleteModel(
            name='PrivacySettings',
        ),
    ]
