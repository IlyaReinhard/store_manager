from django.db import models
import datetime

class Product(models.Model):
    title_of_product = models.CharField(max_length=100, verbose_name='Наименование продукта')
    count_kg_product = models.FloatField(verbose_name='Количество(кг\л)')
    price_of_kg = models.FloatField(verbose_name='Цена (руб) за 1 кг(л)')
    making_date = models.DateField(null=True, blank=True, verbose_name='Дата изготовления')
    expiration_date = models.SmallIntegerField(null=True, blank=True, verbose_name='Срок годности (количество суток)')

    class Meta:
        verbose_name_plural = 'Продукты'


    def __str__(self):
        return self.title_of_product