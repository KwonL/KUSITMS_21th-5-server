# Generated by Django 3.0.6 on 2020-05-24 08:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='foodgallery',
            name='time',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
