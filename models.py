from django.db import models
class event_scheduler(models.Model):
    index = models.Index()
    name = models.TextField()
    date = models.DateField()
    time = models.TimeField()
    description = models.TextField()