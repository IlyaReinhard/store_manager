# Generated by Django 4.0.2 on 2022-02-27 19:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store_mng', '0005_alter_product_count_kg_product'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='expiration_date',
            field=models.SmallIntegerField(blank=True, null=True, verbose_name='Срок годности (количество суток)'),
        ),
    ]
