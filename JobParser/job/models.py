from django.db import models

# Create your models here.


class Vacancy(models.Model):
    job_id = models.BigIntegerField(unique=True)
    href = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    desc = models.TextField(blank=True)
    price = models.CharField(max_length=255, blank=True)
    loc = models.CharField(blank=True, max_length=255)
    is_active = models.BooleanField(default=True)
    time_created = models.DateTimeField(auto_now_add=True)
    time_updated = models.DateTimeField(auto_now=True)


class Resume(models.Model):
    res_id = models.BigIntegerField(unique=True)
    href = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    desc = models.TextField(blank=True)
    price = models.CharField(max_length=255, blank=True)
    bio = models.CharField(blank=True, max_length=255)
    is_active = models.BooleanField(default=True)
    time_created = models.DateTimeField(auto_now_add=True)
    time_updated = models.DateTimeField(auto_now=True)

