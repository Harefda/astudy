# Generated by Django 3.1.7 on 2021-03-10 14:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0016_courselecturedurationtime_seconds'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='lectures_count',
        ),
    ]
