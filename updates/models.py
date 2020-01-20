from django.db import models

# Create your models here.
class Destination(models.Model):
    name= models.CharField(max_length=50)
    img = models.ImageField(upload_to='pics')
    # img = models.ImageField(upload_to='pics', height_field='100px', width_field='100px')
    desc = models.TextField()
    price = models.IntegerField()
    offer = models.BooleanField(default=False)