# Generated by Django 5.0.6 on 2024-07-04 09:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crimsonFilms', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='film',
            name='kID',
            field=models.IntegerField(default=0),
        ),
    ]