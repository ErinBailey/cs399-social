# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import datetime

from django.db import models, migrations
from theatre.models import Show, Actor


def add_movies(app, schema_editor):
    # Adding some initial actors
    tim_cruise = Actor(first_name="Tim", last_name="Cruise",
                       bio="Action thriller-man appearing in popular films such as Highest Gun, A Couple of Good Guys "
                           + "and the Mission Improbable series")
    # Once the data is setup, run save() to store it in the database
    tim_cruise.save()

    malcolm_in_the_middle = Actor(first_name="Malcolm", last_name="In The Middle",
                                  bio="It's unclear whether or not Malcolm was actually under house-arrest during the "
                                      + "filming of \"Distraughtia\" but critics tend to agree that his performance in "
                                      + "\"Robots in Disguise\" was likely his best.")
    malcolm_in_the_middle.save()

    # Create some initial movies
    mission_improb = Show(show_title="Mission Improbable", event_date=datetime.datetime(2015, 3, 1, 17, 0))
    mission_improb.save()
    # Many to many relationships can't be established until the records are both individually saved, so Django's ORM
    # can look up the ID of both objects for the relation table
    mission_improb.main_actors.add(tim_cruise)

    robots = Show(show_title="Robots in Disguise", event_date=datetime.datetime(2015, 2, 15, 15, 0))
    robots.save()
    robots.main_actors.add(malcolm_in_the_middle)



class Migration(migrations.Migration):
    dependencies = [
        ('theatre', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(add_movies),
    ]
