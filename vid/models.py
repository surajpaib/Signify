from __future__ import unicode_literals

from django.db import models
from embed_video.fields import EmbedVideoField


class MyVideo(models.Model):
    url = models.CharField(max_length=300)


class EmbedVideo(models.Model):
    video = EmbedVideoField()