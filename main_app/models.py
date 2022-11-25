from django.core import validators
from django.db import models


class Document(models.Model):
    """
    Модель для хранения загружаемых файлов.
    """
    title = models.CharField(max_length=100)
    file = models.FileField(validators=[validators.FileExtensionValidator(['csv'], message="Только .csv файлы")])
    time_upload = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class ConstructionMaterial(models.Model):
    """
    Модель для сохранения информации которую удалось спарсить.
    """
    code = models.CharField(max_length=10, unique=True, verbose_name='Код')
    name = models.CharField(max_length=150, verbose_name='Наименование')
    level_1 = models.CharField(max_length=150, verbose_name='Уровень1')
    level_2 = models.CharField(blank=True, max_length=150, verbose_name='Уровень2')
    level_3 = models.CharField(blank=True, max_length=150, verbose_name='Уровень3')
    price = models.DecimalField(max_digits=9, decimal_places=2, verbose_name='Цена')
    price_sp = models.DecimalField(max_digits=9, decimal_places=2, verbose_name='ЦенаСП')
    amount = models.FloatField(verbose_name='Количество')
    property = models.TextField(verbose_name='Поля свойств')
    joint_purchases = models.CharField(max_length=150, verbose_name='Совместные покупки')
    measure = models.CharField(max_length=50, verbose_name='Единицы измерения')
    image = models.CharField(max_length=150, verbose_name='Картинка')
    show_on_main = models.BooleanField(verbose_name='Выводить на главной')
    description = models.TextField(blank=True, verbose_name='Описание')
