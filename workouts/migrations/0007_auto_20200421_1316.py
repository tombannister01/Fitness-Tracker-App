# Generated by Django 3.0.5 on 2020-04-21 13:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workouts', '0006_auto_20200421_1306'),
    ]

    operations = [
        migrations.AlterField(
            model_name='muscletraining',
            name='weight',
            field=models.IntegerField(),
        ),
    ]
