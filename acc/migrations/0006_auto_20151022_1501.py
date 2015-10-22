# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('acc', '0005_auto_20151022_1444'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='messages',
            name='recipient',
        ),
        migrations.AddField(
            model_name='messages',
            name='recipient',
            field=models.ForeignKey(to='acc.UserProfile', default=None, related_name='received'),
            preserve_default=False,
        ),
    ]
