from django.db import models


class Crop(models.Model):
    name = models.CharField( max_length = 250, primary_key = True)
    image_url = models.CharField( max_length = 2048 )

class Yield(models.Model):
    key = models.CharField( max_length = 2500, primary_key = True )
    state_name = models.CharField( max_length = 300 )
    district_name = models.CharField( max_length = 300 )
    crop_year = models.IntegerField()
    season = models.CharField( max_length = 300 )
    crop = models.CharField( max_length = 300 )
    area = models.FloatField()
    min_rainfall = models.FloatField()
    max_rainfall = models.FloatField()
    mean_rainfall = models.FloatField()
    annual_rainfall = models.FloatField()
    production = models.FloatField()
