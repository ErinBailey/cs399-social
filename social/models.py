from django.db import models


class User(models.Model):
    user_name = models.CharField(max_length = 30)
    user_dream = models.CharField(max_length = 1000)
    user_flock = models.CharField(max_length = 1000)
    def getusername(self):
        return self.user_name

class Dream(models.Model):
    title = models.CharField(max_length = 120)
    content = models.CharField(max_length = 1000)
    user = models.ForeignKey('User')
    flock = models.CharField(max_length = 32)

class Search(models.Model):
    dream_search = models.CharField(max_length = 30)


    
    

	
