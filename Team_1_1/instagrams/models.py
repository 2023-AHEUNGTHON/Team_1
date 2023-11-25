from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.TextField(verbose_name='title', null=True, blank=True)
    url = models.TextField(verbose_name='url', null=True, blank=True)
