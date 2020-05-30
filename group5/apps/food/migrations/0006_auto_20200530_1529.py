# Generated by Django 3.0.6 on 2020-05-30 06:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0005_foodgallery_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Nutrient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('food_name', models.CharField(max_length=255)),
                ('carbohydrate', models.FloatField()),
                ('protein', models.FloatField()),
                ('fat', models.FloatField()),
                ('salt', models.FloatField()),
                ('kcal', models.FloatField()),
            ],
        ),
        migrations.AddField(
            model_name='foodgallery',
            name='nutrient',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='foods', to='food.Nutrient'),
        ),
    ]