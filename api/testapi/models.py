from django.db import models

#item class


class Items(models.Model):
    title = models.TextField()
    discription = models.TextField()
    persentage = models.DecimalField(max_digits=100,decimal_places=2,default=0.00)
    status = models.BooleanField()
    
    