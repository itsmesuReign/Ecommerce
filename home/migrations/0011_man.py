# Generated by Django 4.0.3 on 2022-04-24 06:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0010_product_is_featured'),
    ]

    operations = [
        migrations.CreateModel(
            name='Man',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, null=True)),
                ('image', models.ImageField(upload_to='man_img/')),
            ],
        ),
    ]
