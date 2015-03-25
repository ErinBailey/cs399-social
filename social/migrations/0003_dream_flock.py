# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('social', '0002_auto_20150324_1720'),
    ]

    operations = [
        migrations.AddField(
            model_name='dream',
            name='flock',
            field=models.CharField(default=2, max_length=32),
            preserve_default=False,
        ),
    ]
