# Generated by Django 2.2.6 on 2019-11-01 18:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog_app', '0007_auto_20191101_2325'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='no_of_dislikes',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='post',
            name='no_of_likes',
            field=models.IntegerField(default=0),
        ),
    ]
