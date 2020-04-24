# Generated by Django 3.0.5 on 2020-04-18 10:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('workouts', '0002_auto_20200418_1027'),
    ]

    operations = [
        migrations.AddField(
            model_name='cardio',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='cardios', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='muscletraining',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='muscle_trainings', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='muscletraining',
            name='duration',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='muscletraining',
            name='speed',
            field=models.IntegerField(null=True),
        ),
    ]
