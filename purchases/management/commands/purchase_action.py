import factory
from django.core.management.base import BaseCommand
from django.utils import timezone

from books.models import Book
from books.tests.util_faker.purchase_factory import PurchaseFactory
from fam.models import Customer
from purchases.models import Purchase


class Command(BaseCommand):
    """
        create fake purchase objects
    """
    help = 'Create fake purchases'

    def add_arguments(self, parser):
        # 1 args== nargs =1
        parser.add_argument('number', nargs='?', type=int, default=2, help='Indicates the number of purchase objects')
        # if action flip-flop: do clear if 'clear' passed
        parser.add_argument(
            '--clear',
            action='store_true',
            default=False,
            dest='clear',
            help='Clear out everything before gen new values'
        )

    def handle(self, *args, **options):
        print('options:', options)
        if options['clear']:
            Purchase.objects.all().delete()
            self.stdout.write(self.style.SUCCESS(f"Deleted all objects = Done"))
        [PurchaseFactory() for _ in range(options['number'])]
        self.stdout.write(self.style.SUCCESS(f"Created {options['number']} purchase objects"))
