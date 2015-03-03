# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('theatre', '0003_auto_20150203_0308'),
    ]

    operations = [
        migrations.CreateModel(
            name='Information',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('performance_information', models.CharField(max_length=1000)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Seat',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('seat_price', models.DecimalField(max_digits=10, decimal_places=2, blank=True)),
                ('seat_discount', models.DecimalField(max_digits=10, decimal_places=2, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='show',
            name='available_seats',
            field=models.IntegerField(max_length=3, default=(100)),
            preserve_default=False,
        ),
    ]
