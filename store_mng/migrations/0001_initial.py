# Generated by Django 4.0.2 on 2022-02-27 19:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title_of_product', models.CharField(max_length=100, verbose_name='Продукты')),
                ('count_kg_product', models.IntegerField(verbose_name='Количество(кг\\л)')),
                ('price_of_kg', models.IntegerField(verbose_name='Цена за 1 кг(л)')),
                ('making_date', models.DateField(blank=True, null=True, verbose_name='Дата изготовления')),
                ('expiration_date', models.SmallIntegerField(blank=True, null=True, verbose_name='Срок годности')),
            ],
        ),
    ]
