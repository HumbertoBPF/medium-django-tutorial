# Generated by Django 4.2.1 on 2023-05-29 15:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('employee_registration', '0003_alter_company_options_company_members_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='company',
            old_name='members',
            new_name='employees',
        ),
    ]