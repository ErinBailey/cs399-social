from django.db import models
from django.contrib.auth.models import User
from django import forms
from social.models import User


class User(models.Model):
    user = models.OneToOneField(User)
    username = models.CharField(max_length = 30)
    email = models.EmailField(default = "")
    password = models.CharField(max_length = 30)
    image = models.ImageField(blank = True)

    
    user_dream = models.CharField(max_length = 1000)
    user_flock = models.CharField(max_length = 1000)

    def __unicode__(self):
        return self.user.username
    def getusername(self):
        return self.username


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model = User
        fields = ('username', 'email', 'password')

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('image',)
        

class Dream(models.Model):
    title = models.CharField(max_length = 120)
    content = models.CharField(max_length = 1000)
    user = models.ForeignKey('User')
    flock = models.CharField(max_length = 32)

class Search(models.Model):
    dream_search = models.CharField(max_length = 30)


    
    

	
