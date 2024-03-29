# Generated by Django 4.1.5 on 2023-01-23 20:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_rename_category_product_category_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='status',
            field=models.BooleanField(default=False, help_text='0=default, 1=Hidden'),
        ),
        migrations.AddField(
            model_name='category',
            name='trending',
            field=models.BooleanField(default=False, help_text='0=default, 1=Trending'),
        ),
        migrations.AddField(
            model_name='subcategory',
            name='status',
            field=models.BooleanField(default=False, help_text='0=default, 1=Hidden'),
        ),
        migrations.AddField(
            model_name='subcategory',
            name='trending',
            field=models.BooleanField(default=False, help_text='0=default, 1=Trending'),
        ),
        migrations.AlterField(
            model_name='product',
            name='subcategory',
            field=models.ForeignKey(default=False, on_delete=django.db.models.deletion.CASCADE, to='store.subcategory'),
        ),
    ]
