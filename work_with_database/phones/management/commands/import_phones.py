import csv

from django.core.management.base import BaseCommand
from phones.models import Phone
from slugify import slugify


class Command(BaseCommand):
    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        with open('phones.csv', 'r') as csvfile:

            phone_reader = csv.DictReader(csvfile, delimiter=';')

            for line in phone_reader:
                slug = slugify(line['name'])

                phone = Phone(
                    name=line['name'],
                    price=line['price'],
                    image=line['image'],
                    release_date=line['release_date'],
                    lte_exists=line['lte_exists'],
                    slug = slug
                )
                phone.save()