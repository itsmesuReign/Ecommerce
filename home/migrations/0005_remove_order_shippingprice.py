# Generated by Django 4.0.3 on 2022-04-20 13:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_remove_product_shippingprice_order_shippingprice'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='shippingPrice',
        ),
    ]
