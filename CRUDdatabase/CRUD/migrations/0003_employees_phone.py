# Generated by Django 4.2.1 on 2023-05-11 08:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CRUD', '0002_employees_delete_post'),
    ]

    operations = [
        migrations.AddField(
            model_name='employees',
            name='phone',
            field=models.IntegerField(null=True),
        ),
    ]