# Generated by Django 3.2 on 2022-08-27 09:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0004_auto_20220827_0920'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='images',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]