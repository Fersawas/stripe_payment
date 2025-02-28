from django.db import models

from constants import NAME_LENGTH, DIGITS, DEC_PLACES, CUR_LENGTH


class Item(models.Model):
    CURRENCY_CHOICES = {"usd": "dollar", "rub": "ruble"}

    name = models.CharField(verbose_name="Наименование", max_length=NAME_LENGTH)
    price = models.DecimalField(
        verbose_name="Цена", max_digits=DIGITS, decimal_places=DEC_PLACES
    )
    description = models.TextField(verbose_name="Описание", blank=True)
    currency = models.CharField(
        verbose_name="Валюта", max_length=CUR_LENGTH, choices=CURRENCY_CHOICES.items()
    )

    def __str__(self) -> str:
        return self.name + " " + str(self.currency) + " " + str(self.price)

    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товары"


class Order(models.Model):
    items = models.ManyToManyField(Item, related_name="orders")
    items_for_delete = models.JSONField(
        verbose_name="Временное хранилище", default=list
    )

    class Meta:
        verbose_name = "Заказ"
        verbose_name_plural = "Заказы"
