# Generated by Django 3.2.3 on 2021-07-12 14:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('billing', '0013_auto_20210712_1347'),
    ]

    operations = [
        migrations.DeleteModel(
            name='PaymentMethod',
        ),
    ]
