# Generated by Django 4.0.3 on 2022-04-24 13:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0017_alter_accessories_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accessories',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='accessories_img/'),
        ),
    ]