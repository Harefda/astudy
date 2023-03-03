# Generated by Django 3.2.3 on 2021-07-09 15:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('billing', '0005_card_postal_code'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='card',
            name='billing_profile',
        ),
        migrations.AddField(
            model_name='card',
            name='billing_profile',
            field=models.ManyToManyField(related_name='cards', to='billing.BillingProfile'),
        ),
    ]
