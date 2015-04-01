# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('social', '0005_user_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('username', models.CharField(max_length=30)),
                ('email', models.EmailField(default=b'', max_length=75)),
                ('password', models.CharField(max_length=30)),
                ('picture', models.ImageField(upload_to=b'profile_images', blank=True)),
                ('user_dream', models.CharField(max_length=1000)),
                ('user_flock', models.CharField(max_length=1000)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='user',
            name='user',
        ),
        migrations.AddField(
            model_name='userprofile',
            name='user',
            field=models.OneToOneField(to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='dream',
            name='user',
            field=models.ForeignKey(to='social.UserProfile'),
            preserve_default=True,
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]
