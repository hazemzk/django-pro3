# Generated by Django 4.2.13 on 2024-06-02 20:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(default='media/img/no_image.jpg', upload_to='products/%Y/%m/%d'),
        ),
    ]
