# Generated by Django 4.0.1 on 2022-03-01 21:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('routine', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userroutine',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='user', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='userexercise',
            name='exercise',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='exercise', to='routine.exercise'),
        ),
        migrations.AddField(
            model_name='userexercise',
            name='workout',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='workout', to='routine.exercise'),
        ),
        migrations.AddField(
            model_name='exercise',
            name='categories',
            field=models.ManyToManyField(to='routine.ExerciseCategory'),
        ),
    ]