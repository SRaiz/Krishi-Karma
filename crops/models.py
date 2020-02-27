from django.db import models


class Crop(models.Model):
    name = models.CharField( max_length = 250 )
    image_url = models.CharField( max_length = 2048 )
