# Generated by Django 4.2.7 on 2023-12-04 00:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('drf', '0006_rename_image_product_image1_remove_product_brand_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fetched_product',
            name='slug',
            field=models.SlugField(blank=True, max_length=100, null=True),
        ),
    ]
