from django.db import models

# Create your models here.
class Products(models.Model):
    title = models.CharField(max_length=120)
    price = models.IntegerField()
    categoty = models.IntegerField()
    #image =

def __str__(self):
    return self.title