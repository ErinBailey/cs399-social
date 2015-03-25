# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('social', '0003_dream_flock'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='user_name',
            new_name='username',
        ),
        migrations.AddField(
            model_name='user',
            name='email',
            field=models.EmailField(default=b'', max_length=75),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='user',
            name='password',
            field=models.CharField(default=1234, max_length=30),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='user',
            field=models.OneToOneField(default=2, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
