from unicodedata import name
from django.db import models

from django.shortcuts import get_object_or_404 
from django.urls import reverse 
from django.contrib.auth.models import User
from django.utils import timezone




# Create your models here.
class Post(models.Model):
    author=models.ForeignKey(User,on_delete=models.CASCADE,null=True) 
    title =models.CharField(max_length=100)
    content=models.TextField(max_length=1000 ,null=True)

    date_posted = models.DateTimeField( default= timezone.now)
    img=models.ImageField(upload_to='core/images/',null=True)
   
    
    def __str__ (self) :
        return   self.title 
    def get_img(self):
        return f"/media/{self.img}" 
    def  get_absolute_url(self):
        return reverse('postdetails',kwargs={'pk':self.pk})    