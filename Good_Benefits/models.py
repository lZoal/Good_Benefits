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


class Image(models.Model):
    title = models.CharField(max_length=30)
    image = models.ImageField(upload_to='themeImages/', height_field=None, width_field=None,blank=True)

    def __str__(self):
        return self.title


class Users(models.Model):
    username=models.CharField(max_length=65,verbose_name="사용자명")

    password=models.CharField(max_length=64,verbose_name="비밀번호")


    def __str__(self):
        return self.username
