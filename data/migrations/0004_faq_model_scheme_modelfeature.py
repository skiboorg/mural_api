# Generated by Django 4.2.6 on 2023-11-03 15:19

import ckeditor_uploader.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0003_remove_product_model_model_categories_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Faq',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=255, null=True)),
                ('description', ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'Faq',
                'verbose_name_plural': 'Faq',
            },
        ),
        migrations.AddField(
            model_name='model',
            name='scheme',
            field=models.IntegerField(default=1, null=True, verbose_name='Использовать схему 1 или 2'),
        ),
        migrations.CreateModel(
            name='ModelFeature',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.CharField(max_length=255, null=True, verbose_name='Название')),
                ('value', models.CharField(max_length=255, null=True, verbose_name='Значение')),
                ('model', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='technical_data', to='data.model')),
            ],
            options={
                'verbose_name': 'Характеристика',
                'verbose_name_plural': 'Характеристики',
            },
        ),
    ]
