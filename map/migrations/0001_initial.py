# Generated by Django 2.2.7 on 2019-11-27 01:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Squirrels',
            fields=[
                ('latitude', models.DecimalField(decimal_places=15, help_text='Latitude', max_digits=19)),
                ('longtitude', models.DecimalField(decimal_places=15, help_text='Longtitude', max_digits=19)),
                ('uid', models.CharField(help_text='Unique Squirrel ID', max_length=255, primary_key=True, serialize=False)),
            ],
        ),
    ]
