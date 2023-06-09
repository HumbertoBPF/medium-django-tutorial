# Generated by Django 4.2.1 on 2023-05-29 15:50

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('employee_registration', '0002_alter_company_foundation_date'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='company',
            options={'verbose_name_plural': 'companies'},
        ),
        migrations.AddField(
            model_name='company',
            name='members',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='company',
            name='branch',
            field=models.CharField(choices=[('IT', 'IT'), ('HEALTH', 'Health'), ('FINANCE', 'Financial market'), ('EDUCATION', 'Education'), ('ENERGY', 'Energy'), ('FOOD', 'Food'), ('OTHER', 'Other')], max_length=255),
        ),
    ]
