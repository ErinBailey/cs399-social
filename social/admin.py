from django.contrib import admin
from social.models import UserProfile, Dream, Search

# Register your models here.
#class SeatsAdmin(admin.ModelSeats):
#	pass
#	admin.site.register(Seats, SeatsAdmin)


admin.site.register(UserProfile)
admin.site.register(Dream)
admin.site.register(Search)

#username: erin
#password: erin

#username: jack
#password: jack