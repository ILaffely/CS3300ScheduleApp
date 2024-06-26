from django.db import models
from django.urls import reverse
# Create your models here.

class EventType (models.Model):
    COLOR = (
        ('blue', 'blue'),
        ('red', 'red'),
        ('green', 'green'),
        ('yellow', 'yellow')
    ) 
    name = models.CharField(max_length = 50)
    color = models.CharField(max_length=200, choices=COLOR, blank = True)
    description = models.TextField(blank=True)
    
     #Default String
    def __str__(self):
        return self.name
    
    
    def get_absolute_url(self):
        return reverse('eventeype-detail', args=[str(self.id)]) 
    


class Event(models.Model):
    type = models.ForeignKey(EventType, on_delete=models.CASCADE, default=None)
    name = models.CharField(max_length=200,blank = True, null = True)
    start_date_time = models.DateTimeField(blank = True, null = True)
    end_date_time = models.DateTimeField(blank = True, null = True)
    description = models.TextField(blank=True)
    
    # Default String
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('event-detail', args=[str(self.id)])