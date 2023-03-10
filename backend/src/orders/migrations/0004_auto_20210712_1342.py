# Generated by Django 3.2.3 on 2021-07-12 10:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('billing', '0012_auto_20210712_1342'),
        ('carts', '0007_auto_20210406_2216'),
        ('orders', '0003_alter_order_order_id'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='order',
            options={'verbose_name': 'Order', 'verbose_name_plural': 'Orders'},
        ),
        migrations.AlterField(
            model_name='order',
            name='billing_profile',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='billing.billingprofile'),
        ),
        migrations.AlterField(
            model_name='order',
            name='cart',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='carts.cart'),
        ),
    ]
