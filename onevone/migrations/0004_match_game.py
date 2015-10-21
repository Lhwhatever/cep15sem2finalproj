# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('onevone', '0003_auto_20151021_1932'),
    ]

    operations = [
        migrations.AddField(
            model_name='match',
            name='game',
            field=models.CharField(max_length=255, default=''),
            preserve_default=False,
        ),
    ]
