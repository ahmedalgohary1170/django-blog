# Generated by Django 4.2 on 2023-11-06 16:59

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_post_publish_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='publish_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
