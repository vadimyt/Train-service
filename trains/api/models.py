# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models

class Cities(models.Model):
    name = models.CharField()

    class Meta:
        # managed = False
        db_table = 'cities'

class Trains(models.Model):
    name = models.CharField()
    count_seat = models.SmallIntegerField()

    class Meta:
        # managed = False
        db_table = 'trains'

class TrainRoutes(models.Model):
    train = models.ForeignKey('Trains', models.DO_NOTHING, db_column='train', blank=True, null=True)
    from_time = models.DateTimeField(blank=True, null=True)
    to_time = models.DateTimeField(blank=True, null=True)
    from_city = models.ForeignKey(Cities, models.DO_NOTHING, db_column='from_city', blank=True, null=True)
    to_city = models.ForeignKey(Cities, models.DO_NOTHING, db_column='to_city', related_name='trainroutes_to_city_set', blank=True, null=True)
    cost = models.BigIntegerField(blank=True, null=True)

    class Meta:
        # managed = False
        db_table = 'train_routes'

class Tickets(models.Model):
    train_route = models.ForeignKey('TrainRoutes', models.DO_NOTHING, db_column='train_route', blank=True, null=True)

    class Meta:
        # managed = False
        db_table = 'tickets'