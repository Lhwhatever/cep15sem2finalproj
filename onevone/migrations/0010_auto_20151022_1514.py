# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('onevone', '0009_auto_20151022_0946'),
    ]

    operations = [
        migrations.AlterField(
            model_name='match',
            name='location',
            field=models.ForeignKey(to='onevone.Location'),
        ),
    ]
