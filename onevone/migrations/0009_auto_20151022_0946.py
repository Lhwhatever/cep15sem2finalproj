# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('onevone', '0008_auto_20151022_0313'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='location',
            name='name',
        ),
        migrations.AddField(
            model_name='location',
            name='loc_name',
            field=models.CharField(default='Club Penguin', verbose_name='Location_Name', max_length=31),
            preserve_default=False,
        ),
    ]
