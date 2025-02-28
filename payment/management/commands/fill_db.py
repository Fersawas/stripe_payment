import sys
from time import sleep, time

from django.core.management.base import BaseCommand, CommandError
from django.db import DEFAULT_DB_ALIAS, connections
from django.db.utils import OperationalError
from payment.models import Item


class Command(BaseCommand):
    help = "Fill the database with sample data"

    def handle(self, *args, **options):
        items = [
            Item(
                name="T-shirt",
                description="T-shirt nice",
                price=50,
                currency="usd",
            ),
            Item(
                name="T-shirt",
                description="T-shirt good enough",
                price=20,
                currency="usd",
            ),
            Item(
                name="Shirt",
                description="Shirt nice",
                price=1200,
                currency="rub",
            ),
            Item(
                name="Shirt", description="Shirt good enough", price=700, currency="rub"
            ),
        ]

        Item.objects.bulk_create(items)
