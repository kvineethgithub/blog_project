# Generated by Django 2.2.6 on 2019-11-02 11:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog_app', '0014_dislike'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post_id', models.CharField(max_length=55, null=True)),
                ('user', models.CharField(max_length=55, null=True)),
                ('comment', models.CharField(max_length=255)),
            ],
        ),
    ]
