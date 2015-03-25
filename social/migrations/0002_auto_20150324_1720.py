# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('social', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dream',
            name='content',
            field=models.CharField(max_length=1000),
            preserve_default=True,
        ),
    ]
