# Generated by Django 4.1.7 on 2023-03-18 14:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Workout', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='workout',
            name='date',
            field=models.DateField(auto_now_add=True),
        ),
    ]
