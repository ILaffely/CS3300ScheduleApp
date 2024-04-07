from django.db import models
from django.urls import reverse
# Create your models here.

class EventType (models.Model):
    COLOR = (
        ('Blue', 'Blue'),
        ('Red', 'Red'),
        ('Green', 'Green'),
        ('Yellow', 'Yellow')
    ) 
    name = models.CharField(max_length = 50)
    color = models.CharField(max_length=200, choices=COLOR, blank = True)
    description = models.TextField(blank=True)
    
     #Default String
    def __str__(self):
        return self.name
    
    
    def get_absolute_url(self):
        return reverse('EventType-detail', args=[str(self.id)]) 
    
