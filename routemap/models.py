from django.contrib.auth.models import User
from django.db import models


class Country(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self):
        return self.name


class Region(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self):
        return self.name


class Route(models.Model):
    starts = models.CharField(max_length=64)
    ends = models.CharField(max_length=64)
    country = models.ForeignKey(Country, on_delete=models.DO_NOTHING, null=True, blank=True)
    region = models.ForeignKey(Region, on_delete=models.DO_NOTHING, null=True, blank=True)
    description = models.TextField()
    surface_condition = models.FloatField()
    surface_condition_votes = models.FloatField(null=True)
    scenic_rating = models.FloatField()
    scenic_rating_votes = models.FloatField(null=True)
    funny_to_drive = models.FloatField()
    funny_to_drive_votes = models.FloatField(null=True)
    overal_rating = models.FloatField()
    overal_rating_votes = models.FloatField(null=True)
    embed_view = models.CharField(max_length=512)


class PhotoSpots(models.Model):
    photo_path = models.ImageField(upload_to="media")
    cordinates = models.CharField(max_length=64, null=True)
    iframe = models.CharField(max_length=1024, null=True)


class RouteList(models.Model):
    name = models.CharField(max_length=128)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    routes = models.ManyToManyField(Route)


from django.contrib import admin


admin.site.register(Country)
admin.site.register(Region)
admin.site.register(Route)
admin.site.register(PhotoSpots)
admin.site.register( RouteList)

