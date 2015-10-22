# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('acc', '0003_auto_20151021_2232'),
    ]

    operations = [
        migrations.AddField(
            model_name='messages',
            name='sent',
            field=models.DateTimeField(verbose_name='Time sent', default=datetime.datetime(2015, 10, 22, 2, 55, 30, 671052, tzinfo=utc), auto_now=True),
            preserve_default=False,
        ),
    ]
