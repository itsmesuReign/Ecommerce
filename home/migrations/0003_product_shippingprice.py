# Generated by Django 4.0.3 on 2022-04-20 13:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_product_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='shippingPrice',
            field=models.FloatField(default=1),
            preserve_default=False,
        ),
    ]
