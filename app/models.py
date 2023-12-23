from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Profile(models.Model):
    BLUE = "bl"
    GREEN = "gr"
    PURPLE = "pu"
    RED = "re"

    TEMPLATE_CHOICES = [
        (BLUE, "blue"),
        (GREEN, "green"),
        (PURPLE, "purple"),
        (RED, "red"),
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    profile_picture = models.ImageField(upload_to='uploads/', null=True)
    description = models.CharField(max_length=250)
    twitter = models.CharField(max_length=100, blank=True)
    github = models.CharField(max_length=100, blank=True)
    linkedin = models.CharField(max_length=100, blank=True)
    template = models.CharField(max_length=2, choices=TEMPLATE_CHOICES, default=BLUE)


class Links(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    Description = models.CharField(max_length=100)
    link = models.CharField(max_length=100)
    times_visited = models.IntegerField(default=0)
