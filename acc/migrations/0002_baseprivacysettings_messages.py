# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('acc', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BasePrivacySettings',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('settings', models.CharField(max_length=2)),
                ('owner', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Messages',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('subject', models.CharField(max_length=255)),
                ('content', models.TextField()),
                ('recipient', models.ForeignKey(related_name='received', to='acc.UserProfile')),
                ('sender', models.ForeignKey(related_name='sended', to='acc.UserProfile')),
            ],
        ),
    ]
