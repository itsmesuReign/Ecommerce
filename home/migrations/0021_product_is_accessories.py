# Generated by Django 4.0.3 on 2022-04-24 13:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0020_remove_accessories_brand'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='is_accessories',
            field=models.BooleanField(default=False),
        ),
    ]
