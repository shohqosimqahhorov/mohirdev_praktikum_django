# Generated by Django 4.0 on 2024-01-17 10:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newsapp', '0005_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='view_count',
            field=models.IntegerField(default=0),
        ),
    ]
