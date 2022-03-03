# Generated by Django 4.0.1 on 2022-03-02 02:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('routine', '0005_alter_userexercise_workout'),
    ]

    operations = [
        migrations.AddField(
            model_name='userroutine',
            name='categories',
            field=models.ManyToManyField(related_name='categories', to='routine.RoutineCategory'),
        ),
        migrations.AddField(
            model_name='userroutine',
            name='private',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='exercise',
            name='categories',
            field=models.ManyToManyField(related_name='routines', to='routine.WorkoutCategory'),
        ),
        migrations.AlterField(
            model_name='userworkout',
            name='routine',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='routines', to='routine.userroutine'),
        ),
    ]