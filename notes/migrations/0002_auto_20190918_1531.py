# Generated by Django 2.2.5 on 2019-09-18 15:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='note',
            name='date_of_creation',
            field=models.DateTimeField(auto_created=True),
        ),
        migrations.AlterField(
            model_name='note',
            name='last_edit',
            field=models.DateTimeField(auto_created=True),
        ),
    ]
