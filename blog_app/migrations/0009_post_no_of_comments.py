# Generated by Django 2.2.6 on 2019-11-01 18:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog_app', '0008_auto_20191101_2330'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='no_of_comments',
            field=models.IntegerField(default=0),
        ),
    ]