# Generated by Django 4.2.6 on 2023-10-25 14:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('green_jacket_app', '0005_favorite_delete_shopcart'),
    ]

    operations = [
        migrations.AddField(
            model_name='brandmodel',
            name='favorite',
            field=models.BooleanField(default=False),
        ),
    ]
