from django.db import models

# Create your models here.




class Vacancy(models.Model):
    out_id = models.BigIntegerField(unique=True)
    href = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    desc = models.TextField(blank=True, null=True)
    price = models.CharField(max_length=255, blank=True, null=True)
    loc = models.CharField(blank=True, max_length=255, null=True)
    is_active = models.BooleanField(default=True)
    time_created = models.DateTimeField(auto_now_add=True)
    time_updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-time_created"]


class Resume(models.Model):
    out_id = models.BigIntegerField(unique=True)
    href = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    desc = models.TextField(blank=True, null=True)
    price = models.CharField(max_length=255, blank=True, null=True)
    bio = models.CharField(blank=True, max_length=255, null=True)
    is_active = models.BooleanField(default=True)
    time_created = models.DateTimeField(auto_now_add=True)
    time_updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-time_created"]


class HHVacancy(models.Model):
    out_id = models.BigIntegerField(unique=True)
    href = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    area = models.CharField(max_length=255)
    salary_from = models.BigIntegerField(blank=True, null=True)
    salary_to = models.BigIntegerField(blank=True, null=True)
    metro = models.CharField(blank=True, max_length=255, null=True)
    req = models.TextField(blank=True, null=True)
    resp = models.TextField(blank=True, null=True)
    is_active = models.BooleanField(default=True)
    time_created = models.DateTimeField(auto_now_add=True)
    time_updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-time_created"]


class HHResume(models.Model):
    out_id = models.BigIntegerField(unique=True)
    href = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    exp = models.CharField(blank=True, null=True, max_length=255)
    price = models.CharField(max_length=255, blank=True, null=True)
    last = models.CharField(blank=True, max_length=255, null=True)
    is_active = models.BooleanField(default=True)
    time_created = models.DateTimeField(auto_now_add=True)
    time_updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-time_created"]