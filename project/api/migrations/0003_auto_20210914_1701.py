# Generated by Django 3.2.7 on 2021-09-14 17:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_review_user_review'),
    ]

    operations = [
        migrations.AddField(
            model_name='watchlist',
            name='avarage_rating',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='watchlist',
            name='number_rating',
            field=models.IntegerField(default=0),
        ),
    ]