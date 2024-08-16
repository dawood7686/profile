from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    profile_picture = models.URLField(max_length=255, null=True, blank=True)
    country_flag = models.URLField(max_length=255, null=True, blank=True)
    business_type = models.CharField(max_length=255, null=True, blank=True)
    patriot = models.BooleanField(default=False)
    description = models.TextField(null=True, blank=True)
    social_links = models.JSONField(default=list, blank=True)
    social_media_screenshots = models.JSONField(default=list, blank=True)
    connected_persons = models.JSONField( blank=True)
    personal_details = models.JSONField( blank=True)
    news_screenshots = models.JSONField(default=list, blank=True)
