# Generated by Django 4.2.6 on 2023-10-24 14:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('image_url', models.CharField(max_length=5000)),
            ],
        ),
        migrations.CreateModel(
            name='BuildProcess',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('image_url', models.CharField(max_length=5000)),
                ('score', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('image_url', models.CharField(max_length=5000)),
                ('score', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Material',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('image_url', models.CharField(max_length=5000)),
                ('score', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='UserCustom',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('dark_mode', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='ShopCart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='shop_carts', to='green_jacket_app.usercustom')),
            ],
        ),
        migrations.CreateModel(
            name='BrandModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('name', models.CharField(max_length=50)),
                ('type', models.CharField(max_length=50)),
                ('link', models.CharField(max_length=500)),
                ('brand', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='brand_models', to='green_jacket_app.brand')),
                ('build_process', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='brand_models', to='green_jacket_app.buildprocess')),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='brand_models', to='green_jacket_app.country')),
                ('material', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='brand_models', to='green_jacket_app.material')),
                ('shop_cart', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='brand_models', to='green_jacket_app.shopcart')),
            ],
        ),
    ]
