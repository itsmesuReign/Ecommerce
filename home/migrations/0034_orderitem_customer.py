# Generated by Django 4.0.3 on 2022-05-09 17:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0033_ordered'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderitem',
            name='customer',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='home.customer'),
        ),
    ]
