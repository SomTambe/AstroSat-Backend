from django.db import models

# Create your models here.

class source(models.Model):
    ra = models.FloatField()
    dec = models.FloatField()
    name = models.CharField(max_length=100, unique=True)
    pubs = models.ManyToManyField('pub.pubs', blank = True)

    def __str__(self):
        return self.name
