# Generated by Django 2.0.13 on 2019-08-17 16:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='game',
            name='game_id',
        ),
        migrations.AlterField(
            model_name='game',
            name='editors_choice',
            field=models.BooleanField(default=False),
        ),
    ]
