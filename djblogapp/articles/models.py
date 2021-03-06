# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Article(models.Model):
    title =models.CharField(max_length=50)
    slug = models.SlugField()
    body=models.TextField(max_length=140)
    date=models.DateTimeField(auto_now_add=True)
    # add in thumbnail later
    # add in author later

    def __unicode__(self):
        return self.title

    def snippet(self):
        return self.body[50]