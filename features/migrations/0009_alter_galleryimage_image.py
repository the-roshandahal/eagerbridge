# Generated by Django 4.1.4 on 2023-04-15 17:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('features', '0008_remove_gallery_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='galleryimage',
            name='image',
            field=models.ImageField(upload_to='gallery_images/', verbose_name='Image (670*670)'),
        ),
    ]
