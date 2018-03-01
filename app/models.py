"""
Definition of models.
"""

from django.db import models

# Create your models here.
# kevin.cheng kevin.cheng@omniad.com.tw w0rdPass

#https://djangogirlstaipei.gitbooks.io/django-girls-taipei-tutorial/django/models.html
class Post(models.Model):
    title= models.CharField(max_length= 100)
    content= models.TextField(blank= True)
    photo= models.TextField(blank= True)
    location= models.CharField(max_length= 100)
    created_at= models.DateTimeField(auto_now_add= True)
    updated_at= models.DateTimeField(auto_now= True)

#