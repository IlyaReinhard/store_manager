# Generated by Django 4.0.2 on 2022-02-28 16:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store_mng', '0007_alter_product_price_of_kg'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='product',
            options={'verbose_name_plural': 'Продукты'},
        ),
        migrations.AlterField(
            model_name='product',
            name='expiration_date',
            field=models.DateField(blank=True, null=True, verbose_name='Срок годности (количество суток)'),
        ),
    ]
