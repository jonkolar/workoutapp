# Generated by Django 4.0.3 on 2022-03-11 03:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('routine', '0007_rename_private_userroutine_is_private_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userexercise',
            name='workout',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='user_workout', to='routine.userworkout'),
        ),
    ]