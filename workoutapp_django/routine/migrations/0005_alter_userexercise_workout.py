# Generated by Django 4.0.1 on 2022-03-01 21:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('routine', '0004_delete_exercisecategory_alter_exercise_categories'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userexercise',
            name='workout',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='workout', to='routine.userworkout'),
        ),
    ]
