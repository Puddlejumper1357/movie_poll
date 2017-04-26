from __future__ import unicode_literals
from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey

# Create your models here.

class Movies(models.Model):
    Movie_Title = models.CharField(max_length=200)
    image = models.ImageField(null=True, blank=True)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.Movie_Title

class Choice(models.Model):
    question = models.ForeignKey(Movies, on_delete=models.CASCADE)
    choice_text = models.IntegerField(default=3)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.Movie_Title

    