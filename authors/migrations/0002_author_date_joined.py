# Generated by Django 4.0.6 on 2022-07-06 07:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authors', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='date_joined',
            field=models.DateField(auto_now_add=True, null=True),
        ),
    ]
