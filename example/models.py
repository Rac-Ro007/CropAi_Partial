from django.db import models
from django.utils import timezone

# Create your models here.

class Crops(models.Model):
	Crop_name = models.CharField(max_length=100)
	start_date = models.DateTimeField(default=timezone.now)

def __str__(self):
	return self.name
