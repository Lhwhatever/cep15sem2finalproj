# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('acc', '0002_baseprivacysettings_messages'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='baseprivacysettings',
            name='owner',
        ),
        migrations.DeleteModel(
            name='BasePrivacySettings',
        ),
    ]
