from django.db import models

# Model to store some popular actors that star in movies
class Actor(models.Model):
    # Keep names separate in case we want to query against just part of the name
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    # Short description bio about the actor
    bio = models.TextField(null=True)

# Model to store movie objects
class Show(models.Model):	
	# Numeric field for the number of available seats for a given show
	available_seats = models.IntegerField(max_length=3)
	show_title = models.CharField(max_length=100)
	# TextField to hold showtimes, nullable in case we create a movie record for a film that isn't out yet
	event_date = models.DateTimeField()
	# Many to many relationship with actors, since we could add actor records for multiple actors in a movie
	main_actors = models.ManyToManyField(Actor)

# Model to store the Theatre Seat objects
class Seat(models.Model):	
	# Currency field to hold the price of the seat in a given section
	seat_price = models.DecimalField(max_digits=10, decimal_places=2, blank=True)
	# Currency field to hold the value of the discount if person purchasing the ticket is a Student/Military
	seat_discount = models.DecimalField(max_digits=10, decimal_places=2, blank=True)
	
#Model To describe each movie
class Information(models.Model):
        performance_information = models.CharField(max_length=1000)	

	