from django.db import models


class User(models.Model):
    user_name = models.CharField(max_length = 30)
    user_dream = models.CharField(max_length = 1000)
    user_flock = models.CharField(max_length = 1000)

class Dream(models.Model):
    dream = models.CharField(max_length = 120)

class Search(models.Model):
    dream_search = models.CharField(max_length = 30)


    
    

	
