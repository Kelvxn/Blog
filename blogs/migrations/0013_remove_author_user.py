# Generated by Django 3.2.9 on 2022-04-17 20:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0012_rename_username_author_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='author',
            name='user',
        ),
    ]
