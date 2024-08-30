from django.db import models

# Create your models here.
class TrainRoute(models.Model):
    id = models.IntegerField(primary_key=True)
    from_city = models.CharField(max_length=100)
    from_time = models.CharField(max_length=100)
    to_city = models.CharField(max_length=100)
    to_time = models.CharField(max_length=100)
    cost = models.IntegerField()