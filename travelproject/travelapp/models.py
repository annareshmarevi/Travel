from django.db import models

# Create your models here.
class Place(models.Model):
    name=models.CharField(max_length=250)
    img=models.ImageField(upload_to='pics')
    desc=models.TextField()

    def __str__(self):
        return self.name

class Guide(models.Model):
    gimg=models.ImageField(upload_to='gpics')
    gname=models.CharField(max_length=250)
    gdesign=models.CharField(max_length=250)

    def __str__(self):
        return self.gname