# Generated by Django 4.0.1 on 2022-01-27 01:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('routine', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='workoutexercise',
            name='order',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(max_length=150, unique=True),
        ),
    ]
