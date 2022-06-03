from django.contrib.auth.models import User
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
    voter = models.ManyToManyField(User, blank=True, related_name='voter_post')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return f'/place/{self.title}/'


class Comment(models.Model):
    place = models.ForeignKey(Place, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.author}::{self.content}'

    def get_absolute_url(self):
        return f'{self.place.get_absolute_url()}#comment-{self.pk}'

    def delete_url(self):
        return f'/place/comment/delete/{self.pk}'

    def modify_url(self):
        return f'/place/comment/modify/{self.pk}'