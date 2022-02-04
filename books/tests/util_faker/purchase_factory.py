import random

import factory

from books.tests.util_faker.book_factory import BookFactory
from purchases.models import Purchase
from fam.models import Customer


class CustomerFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Customer

    name = factory.Faker('name')
    email = factory.Faker('email')
    address = factory.Faker('street_address')

    city = factory.Faker('city')
    country = factory.Faker('country')
    postal_code = factory.Faker('postalcode')

    @factory.lazy_attribute
    def address_2(self):
        if random.choice([0] * 9 + [1]):
            return factory.Faker('secondary_address')
        return ''


class PurchaseFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Purchase

    customer = factory.SubFactory(CustomerFactory)
    placed_at = factory.Faker(
        'date_time_this_year',
        after_now=False,
        before_now=True
    )

    @factory.post_generation
    def books(self, created, extracted, **kwargs):
        if created:
            some_books = BookFactory.create_batch(size=random.randint(2, 5))

            for book in some_books:
                # print(book.price)
                print('created book with title', book.title)
                # self.books.add(book)
            return
        if extracted:
            for book in extracted:
                self.books.add(book)
