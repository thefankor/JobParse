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
    bio = models.TextField(blank=True, max_length=255, null=True)
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
    experience = models.CharField(choices=(
            ("noExperience", "Без опыта"),
            ("between1And3", "От 1 года до 3 лет"),
            ("between3And6", "От 3 до 6 лет"),
            ("moreThan6", "Более 6 лет"),
        ),
        default="noExperience", blank=True, null=True, max_length=30)
    employment = models.CharField(choices=(
            ("full", "Полная занятость"),
            ("part", "Частичная занятость"),
            ("project", "Проектная работа"),
            ("volunteer", "Волонтерство"),
            ("probation", "Стажировка"),
        ),
        default="full", blank=True, null=True, max_length=30)

    class Meta:
        ordering = ["-time_updated"]


class HHResume(models.Model):
    out_id = models.BigIntegerField(unique=True)
    href = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    exp = models.CharField(blank=True, null=True, max_length=255)
    price = models.BigIntegerField(blank=True, null=True)
    last = models.CharField(blank=True, max_length=255, null=True)
    is_active = models.BooleanField(default=True)
    time_created = models.DateTimeField(auto_now_add=True)
    time_updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-time_created"]