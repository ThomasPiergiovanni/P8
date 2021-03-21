# Generated by Django 3.1.7 on 2021-03-21 17:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('supersub', '0012_product_product_category'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='product_category',
            new_name='compose_product_category',
        ),
        migrations.RemoveField(
            model_name='user',
            name='favorites',
        ),
        migrations.CreateModel(
            name='Favorites',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('favorites', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='supersub.productcategory')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='supersub.user')),
            ],
        ),
        migrations.AddField(
            model_name='user',
            name='compose_favorites',
            field=models.ManyToManyField(through='supersub.Favorites', to='supersub.ProductCategory'),
        ),
    ]
