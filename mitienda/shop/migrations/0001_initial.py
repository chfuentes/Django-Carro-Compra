# Generated by Django 4.1 on 2024-11-10 13:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200)),
                ('slug', models.SlugField(max_length=200, unique=True)),
            ],
            options={
                'verbose_name': 'categoria',
                'verbose_name_plural': 'categorias',
                'ordering': ['nombre'],
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200)),
                ('slug', models.SlugField(max_length=200)),
                ('imagen', models.ImageField(blank=True, upload_to='productos/%Y/%m/%d')),
                ('descripcion', models.TextField(blank=True)),
                ('precio', models.DecimalField(decimal_places=2, max_digits=10)),
                ('disponible', models.BooleanField(default=True)),
                ('creado', models.DateTimeField(auto_now_add=True)),
                ('actualizado', models.DateTimeField(auto_now=True)),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='productos', to='shop.categoria')),
            ],
            options={
                'ordering': ['nombre'],
            },
        ),
        migrations.AddIndex(
            model_name='categoria',
            index=models.Index(fields=['nombre'], name='shop_catego_nombre_a77332_idx'),
        ),
        migrations.AddIndex(
            model_name='product',
            index=models.Index(fields=['id', 'slug'], name='shop_produc_id_f21274_idx'),
        ),
        migrations.AddIndex(
            model_name='product',
            index=models.Index(fields=['nombre'], name='shop_produc_nombre_fe90c6_idx'),
        ),
        migrations.AddIndex(
            model_name='product',
            index=models.Index(fields=['-creado'], name='shop_produc_creado_738c9a_idx'),
        ),
    ]