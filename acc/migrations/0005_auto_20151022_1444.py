# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('acc', '0004_messages_sent'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='messages',
            name='recipient',
        ),
        migrations.AddField(
            model_name='messages',
            name='recipient',
            field=models.ManyToManyField(to='acc.UserProfile', related_name='received'),
        ),
    ]
