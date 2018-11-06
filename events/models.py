from django.db import models

# Create your models here.

class Event(models.Model):
    name = models.CharField("Name of Event",max_length = 100,default = "")
    description = models.TextField("Description",max_length = 2000, blank = True)
    max_slots = models.IntegerField("Max Slots",blank=True, default = 0)
    date_from = models.DateField('Start Date')
    date_to = models.DateField("End Date")
    time_from = models.TimeField("Start Time")
    time_to = models.TimeField("End Time")
    venue=models.CharField("Venue", max_length = 100)
    date_created = models.DateTimeField("date Created", auto_now_add=True )
    

def _str_(self):
    return self.name