from django.db import models

class Event(models.Model):
    EVENT_TYPES = [
        ('music', 'Music'),
        ('sports', 'Sports'),
        ('conference', 'Conference'),
        ('workshop', 'Workshop'),
        ('celebration','Celebration')
    ]

    event_name = models.CharField(max_length=200)
    event_type = models.CharField(max_length=50, choices=EVENT_TYPES)
    description = models.TextField(blank=True, null=True)
    location = models.CharField(max_length=200)
    date = models.DateField()
    time = models.TimeField()
    entry_fee = models.PositiveIntegerField(default=0)

