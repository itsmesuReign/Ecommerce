# Generated by Django 4.0.3 on 2022-04-24 05:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0009_customer_device'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='is_featured',
            field=models.BooleanField(default=False),
        ),
    ]
