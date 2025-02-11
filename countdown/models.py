from django.db import models

class Event(models.Model):
    name = models.CharField(max_length=255)  # Event name
    event_date = models.DateTimeField()  # Event date and time

    def __str__(self):
        return self.name
