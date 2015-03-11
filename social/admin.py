from django.contrib import admin
from social.models import User, Dream, Search

# Register your models here.
#class SeatsAdmin(admin.ModelSeats):
#	pass
#	admin.site.register(Seats, SeatsAdmin)


admin.site.register(User)
admin.site.register(Dream)
admin.site.register(Search)
