# Generated by Django 4.0.4 on 2022-06-03 11:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0003_product_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.FileField(default=1, upload_to='resources/product'),
            preserve_default=False,
        ),
    ]
