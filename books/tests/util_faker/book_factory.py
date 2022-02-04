import factory
import faker
from books.models import Book, Author
from .authors import AUTHORS
from books.models import POETRY, ROMANCE, SCF

fk = faker.Faker()


class AuthorFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Author

    name = factory.Iterator(AUTHORS)


class BookFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Book

    title = factory.lazy_attribute(lambda _: ' '.join(fk.words(nb=3)).title())
    author = factory.SubFactory(AuthorFactory)
    genre = factory.Iterator([POETRY, SCF, ROMANCE])
    price = factory.lazy_attribute(
        lambda _: fk.pydecimal(left_digits=4, right_digits=2, max_value=1000, min_value=00.00))
    isbn = factory.Faker('isbn10')
    sale = factory.Faker('pybool')
