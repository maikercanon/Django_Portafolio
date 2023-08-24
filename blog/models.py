from django.db import models
import datetime 
# Create your models here.
class Post(models.Model):
    title=models.CharField(max_length=200)
    description=models.TextField()
    imagen=models.ImageField(upload_to='blog/images/')
    #si no agrega fecha el datetime me pone la del momento
    date=models.DateField(datetime.date.today)
    objects=models.Manager()
