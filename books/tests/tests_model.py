from django.test import TestCase
from books.tests.util_faker.book_factory import BookFactory
from books.tests.util_faker.authors import AUTHORS
from books.tests.util_faker.purchase_factory import PurchaseFactory


class BookTest(TestCase):
    def setUp(self) -> None:
        self.book = BookFactory()

    def test_book_slug(self):
        # print(self.book.slug)
        self.assertNotEqual(self.book.slug, '')
        self.assertIn(self.book.author.name, AUTHORS)


class PurchaseTest(TestCase):
    def setUp(self) -> None:
        self.purchases = PurchaseFactory()
        print('my purcheses are:', self.purchases)

    def test_purchase_basic(self):
        self.assertGreater(self.purchases.books.count(), 0)

    def test_total(self):
        total = 0
        for book in self.purchases.books.all():
            print('price is', book.price)
            print(type(book.price))
            total += book.price
        self.assertEqual(total, self.purchases.total)
