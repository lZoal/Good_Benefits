from django.db import models


class Feed(models.Model):
    content = models.TextField()
    image = models.TextField()
    profile_image = models.TextField()
    user_id = models.TextField()
    view_count = models.IntegerField()


class RecommendPeople(models.Model):
    user_id = models.TextField()
    profile_image = models.TextField()
    comment = models.TextField()
