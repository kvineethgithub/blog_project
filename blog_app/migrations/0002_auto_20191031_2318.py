# Generated by Django 2.2.6 on 2019-10-31 17:48

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='BlogPost',
            new_name='Post',
        ),
    ]
