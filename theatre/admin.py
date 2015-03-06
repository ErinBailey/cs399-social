from django.contrib import admin
from theatre.models import Seat, Actor, Show, Information, User, Dream, Search

# Register your models here.
#class SeatsAdmin(admin.ModelSeats):
#	pass
#	admin.site.register(Seats, SeatsAdmin)

admin.site.register(Seat)
admin.site.register(Actor)
admin.site.register(Show)
admin.site.register(Information)
admin.site.register(User)
admin.site.register(Dream)
admin.site.register(Search)