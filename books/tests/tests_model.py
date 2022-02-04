from django.test import TestCase
from django.utils import timezone

from books.tests.util_faker.book_factory import BookFactory
from books.tests.util_faker.authors import AUTHORS
from books.tests.util_faker.purchase_factory import PurchaseFactory


class BookTest(TestCase):
    def setUp(self) -> None:
        self.book = BookFactory()

    def test_book_slug(self):
        self.assertNotEqual(self.book.slug, '')
        self.assertIn(self.book.author.name, AUTHORS)


class PurchaseTest(TestCase):
    def setUp(self) -> None:
        self.purchase = PurchaseFactory()

    def test_purchase_book_count(self):
        self.assertGreater(self.purchase.books.count(), 0)

    def test_total(self):
        total = 0
        for book in self.purchase.books.all():
            total += book.price
        self.assertEqual(total, self.purchase.total)
