# Generated by Django 4.0.3 on 2022-05-09 17:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0035_remove_orderitem_customer_ordered_customer'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orderitem',
            name='order',
        ),
    ]