from django.db import models

# Create your models here.

class user(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    phone = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    gender = models.CharField(max_length=50)
    create_date = models.DateField(auto_now_add=True)
    country = models.CharField(max_length=50,null=True,blank=True)
    state = models.CharField(max_length=50,null=True,blank=True)
    dob = models.DateField(auto_now=True,null=True,blank=True)
    about = models.TextField(null=True,blank=True)
    height = models.CharField(max_length=50,null=True,blank=True)
    hobbies = models.CharField(max_length=50,null=True,blank=True)
    alcohol = models.BooleanField(default=False)
    smoke = models.BooleanField(default=False)
    relationship = models.CharField(max_length=50,null=True,blank=True)
    languages = models.CharField(max_length=50,null=True,blank=True)
    update_date = models.DateField(auto_now=True,null=True,blank=True)

