# Generated by Django 4.2.1 on 2023-05-11 08:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('CRUD', '0003_employees_phone'),
    ]

    operations = [
        migrations.RenameField(
            model_name='employees',
            old_name='phone',
            new_name='phone_emp',
        ),
    ]
