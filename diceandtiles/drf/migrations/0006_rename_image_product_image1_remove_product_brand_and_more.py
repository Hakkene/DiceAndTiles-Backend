# Generated by Django 4.2.7 on 2023-12-03 22:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('drf', '0005_vote'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='image',
            new_name='image1',
        ),
        migrations.RemoveField(
            model_name='product',
            name='brand',
        ),
        migrations.AddField(
            model_name='product',
            name='bggid',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='image2',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
        migrations.AddField(
            model_name='product',
            name='image3',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
        migrations.AddField(
            model_name='product',
            name='image4',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
        migrations.AddField(
            model_name='product',
            name='image5',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
        migrations.AddField(
            model_name='product',
            name='image_url',
            field=models.URLField(blank=True),
        ),
        migrations.AddField(
            model_name='product',
            name='max_players',
            field=models.IntegerField(blank=True, default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='min_players',
            field=models.IntegerField(blank=True, default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='thumbnail',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
        migrations.AddField(
            model_name='product',
            name='thumbnail_url',
            field=models.URLField(blank=True),
        ),
        migrations.CreateModel(
            name='Fetched_Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bggid', models.IntegerField(blank=True, null=True)),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True)),
                ('slug', models.SlugField(blank=True, max_length=100)),
                ('min_players', models.IntegerField(blank=True, null=True)),
                ('max_players', models.IntegerField(blank=True, null=True)),
                ('image_url', models.URLField(blank=True)),
                ('thumbnail_url', models.URLField(blank=True)),
                ('category', models.ManyToManyField(blank=True, to='drf.category')),
            ],
        ),
    ]
