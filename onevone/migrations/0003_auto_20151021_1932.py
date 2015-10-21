# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('onevone', '0002_auto_20151021_1855'),
    ]

    operations = [
        migrations.AddField(
            model_name='gamecategory',
            name='label',
            field=models.CharField(default='test', max_length=15),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='gamecategory',
            name='name',
            field=models.CharField(max_length=63),
        ),
    ]
