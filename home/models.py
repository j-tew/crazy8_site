from django.db import models

# Create your models here.
class Gig(models.Model):
    artist = models.CharField(max_length=80)
    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()

    def __str__(self):
        return self.title