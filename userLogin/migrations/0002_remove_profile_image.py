# Generated by Django 2.2.5 on 2020-01-29 14:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userLogin', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='image',
        ),
    ]