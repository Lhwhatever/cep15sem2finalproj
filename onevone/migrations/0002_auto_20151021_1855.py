# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('onevone', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gamecategory',
            name='games',
            field=models.ForeignKey(to='onevone.Match', null=True, blank=True),
        ),
    ]
