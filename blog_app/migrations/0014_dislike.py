# Generated by Django 2.2.6 on 2019-11-02 10:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog_app', '0013_auto_20191102_1534'),
    ]

    operations = [
        migrations.CreateModel(
            name='Dislike',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post_id', models.CharField(max_length=55, null=True)),
                ('user', models.CharField(max_length=55, null=True)),
            ],
        ),
    ]