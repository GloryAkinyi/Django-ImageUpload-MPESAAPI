# Generated by Django 4.2.7 on 2023-11-05 11:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0005_alter_product_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(default='logo.png', upload_to='images'),
        ),
    ]