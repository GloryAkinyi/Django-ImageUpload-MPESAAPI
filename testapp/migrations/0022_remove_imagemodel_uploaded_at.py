# Generated by Django 4.2.7 on 2023-11-14 09:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0021_alter_imagemodel_price_alter_imagemodel_title'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='imagemodel',
            name='uploaded_at',
        ),
    ]
