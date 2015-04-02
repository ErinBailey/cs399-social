# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('social', '0006_auto_20150401_0435'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='user_dream',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='user_flock',
        ),
    ]
