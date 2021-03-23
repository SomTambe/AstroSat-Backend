from django.db import models

# Create your models here.

"""
class source(models.Model)

Django model for a given astronomical source. Contains the essential fields like ra, 
dec, source name, if it has been observed by astrosat or not, list of publications.

"""
# ra
# dec
# Fx(uJy)
# Porb
# SIMBAD_Name
# Final_Type
# Astrosat_Flag
# Date_Observed
# Time_Observed
# Proposal_ID
# Target_ID
# Observation_ID
# Instrument
# Publications

class source(models.Model):
    ra = models.FloatField()
    dec = models.FloatField()
    name = models.CharField(max_length=100, unique=True)
    pubs = models.ManyToManyField('pub.pubs', blank = True)
    astrosat = models.BooleanField(default=False)
    dateobs = models.CharField(max_length=15, default='Not Available')
    timeobs = models.CharField(max_length=15, default='Not Available')
    srctype = models.CharField(max_length=100, default='Not Available')
    prop_id = models.CharField(max_length=15, default='Not Available')
    obs_id = models.CharField(max_length=100, default='Not Available')
    tgt_id = models.CharField(max_length=15, default='Not Available')
    instrument = models.CharField(max_length=100, default='Not Available')
    porb = models.CharField(max_length=100, default='Not Available') # unit = days
    flux = models.FloatField(null=True, blank=True, default=None) # Average X-ray flux (2-10keV), unit = MicroJansky

    def __str__(self):
        return self.name
