# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('onevone', '0005_auto_20151021_2327'),
    ]

    operations = [
        migrations.AlterField(
            model_name='match',
            name='category',
            field=models.ForeignKey(to='onevone.GameCategory'),
        ),
    ]
