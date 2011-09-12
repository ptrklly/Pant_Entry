from django.db import models

# Create your models here.

from django.db import models

class Pant(models.Model):
    type = models.CharField(max_length = 100, blank = True, null= True, default="None")
    ref_id = models.CharField(max_length = 100, blank=True, null=True, default="None")
    waist_listed  = models.FloatField(blank=True, null=True)
    length_listed  = models.FloatField(blank=True, null=True)
    front_rise  = models.FloatField(blank=True, null=True, default=0)
    back_rise  = models.FloatField(blank=True, null=True)
    leg_opening  = models.FloatField(blank=True, null=True)
    waist  = models.FloatField(blank=True, null=True)
    in_seam  = models.FloatField(blank=True, null=True)
    out_seam = models.FloatField(blank=True, null=True)
    brand = models.CharField(max_length= 100, blank=True, null=True)
    style = models.CharField(max_length= 300, blank=True, null=True)
    description = models.CharField(max_length=10000, blank=True, null=True)
    def __unicode__(self):
        return self.type



class Feedback(models.Model):
    subject = models.CharField(max_length=1000)
    message = models.CharField(max_length=2000, blank=True, null=True)
    sender = models.EmailField(blank=True, null=True)
    def __unicode__(self):
        return self.subject

class Inquiry(models.Model):
    question = models.CharField(max_length=1000)
    response = models.CharField(max_length=2000, blank=True, null=True)
    responder = models.CharField(max_length=50, blank=True, null=True)
    def __unicode__(self):
        return self.question

class Item(models.Model):
    brand = models.CharField(max_length= 100, blank=True, null=True)
    style = models.CharField(max_length= 300, blank=True, null=True)
    desc = models.CharField(max_length=10000, blank=True, null=True)
    waist = models.CharField(max_length= 300, blank=True, null=True)
    rise = models.CharField(max_length=300, blank=True, null=True)
    cuff = models.CharField(max_length=300, blank=True, null=True)
    thigh = models.CharField(max_length=300, blank=True, null=True)
    pic = models.CharField(max_length= 300, blank=True, null=True)
    price = models.CharField(max_length= 300, blank=True, null=True)
    similarity = models.CharField(max_length=5, blank= True, null=True)
    sale = models.CharField(max_length=20, blank=True, null=True)
    color1 = models.CharField(max_length=50, blank=True, null=True)
    color2 = models.CharField(max_length=50, blank=True,null=True)
    color3 = models.CharField(max_length=50, blank=True,null=True)
    color4 = models.CharField(max_length=50, blank=True,null=True)

    def __unicode__(self):
        return self.brand

