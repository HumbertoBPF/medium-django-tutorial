from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone


class Company(models.Model):
    TYPE_CHOICES = [
        ("IT", "IT"),
        ("HEALTH", "Health"),
        ("FINANCE", "Financial market"),
        ("EDUCATION", "Education"),
        ("ENERGY", "Energy"),
        ("FOOD", "Food"),
        ("OTHER", "Other")
    ]
    name = models.CharField(max_length=255)
    address = models.TextField()
    foundation_date = models.DateField(default=timezone.now)
    domain = models.CharField(max_length=255, choices=TYPE_CHOICES)
    employees = models.ManyToManyField(User)

    class Meta:
        verbose_name_plural = "companies"

    def __str__(self):
        return self.name
