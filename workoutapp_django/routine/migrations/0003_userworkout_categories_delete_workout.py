# Generated by Django 4.0.1 on 2022-03-01 21:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('routine', '0002_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userworkout',
            name='categories',
            field=models.ManyToManyField(to='routine.WorkoutCategory'),
        ),
        migrations.DeleteModel(
            name='Workout',
        ),
    ]
