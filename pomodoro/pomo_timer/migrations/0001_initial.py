# Generated by Django 4.2.7 on 2023-11-30 20:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='timers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pomodoro', models.IntegerField(default=25)),
                ('long_break', models.IntegerField(default=15)),
                ('short_break', models.IntegerField(default=5)),
            ],
        ),
    ]
