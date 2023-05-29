from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone


class Company(models.Model):
    # First item: content to be stored in the actual table
    # Second item: string to be rendered on the admin page
    TYPE_CHOICES = [
        ("IT", "IT"),
        ("HEALTH", "Health"),
        ("FINANCE", "Financial market"),
        ("EDUCATION", "Education"),
        ("ENERGY", "Energy"),
        ("FOOD", "Food"),
        ("OTHER", "Other")
    ]

    # CharField: used for small-medium texts (requires a "max_length" attr)
    name = models.CharField(max_length=255)
    # TextField: used for larger texts
    address = models.TextField()
    # DateTime: used for dates
    foundation_date = models.DateField(default=timezone.now)
    # "choices" attribute: used to only allow certain texts
    branch = models.CharField(max_length=255, choices=TYPE_CHOICES)
    # Relationship between User and Company table
    # It's many from the company side, because a company can have many users as employees
    # It's many from the user side, because a user can work for many companies
    employees = models.ManyToManyField(User)

    class Meta:
        # String to be used when the plural version of the table name is needed
        verbose_name_plural = "companies"

    def __str__(self):
        # String providing the textual representation of the table records
        return self.name
