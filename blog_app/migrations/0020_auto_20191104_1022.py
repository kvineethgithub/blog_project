# Generated by Django 2.2.6 on 2019-11-04 04:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog_app', '0019_auto_20191104_1017'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='commented_user',
            new_name='user',
        ),
        migrations.RenameField(
            model_name='dislike',
            old_name='disliked_user',
            new_name='user',
        ),
        migrations.RenameField(
            model_name='like',
            old_name='liked_user',
            new_name='user',
        ),
    ]
