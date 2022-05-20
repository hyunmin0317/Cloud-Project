from django.db import models

class Place(models.Model):
    title = models.CharField(max_length=255)
    address = models.CharField(max_length=255, null=True)
    roadAddress = models.CharField(max_length=255, null=True)
    category = models.CharField(max_length=255, null=True)
    image = models.URLField(null=True)
    website = models.URLField(null=True)
    mapx = models.IntegerField(null=True)
    mapy = models.IntegerField(null=True)

    def __str__(self):
        return self.title