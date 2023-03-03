# Generated by Django 3.2.3 on 2021-07-08 10:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('billing', '0005_card_postal_code'),
        ('carts', '0007_auto_20210406_2216'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_id', models.CharField(blank=True, max_length=120)),
                ('total', models.DecimalField(decimal_places=2, default=0.0, max_digits=100)),
                ('paid', models.BooleanField(default=False)),
                ('shipped', models.BooleanField(default=False)),
                ('returned', models.BooleanField(default=False)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('billing_profile', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='billing.billingprofile')),
                ('cart', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='carts.cart')),
            ],
            options={
                'verbose_name': 'Billing profile',
                'verbose_name_plural': 'Billing profiles',
            },
        ),
    ]