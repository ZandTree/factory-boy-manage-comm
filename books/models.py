from django.db import models
from autoslug import AutoSlugField

# for faker and factory boy obj: to avoid tuples
POETRY = 'poetry'
ROMANCE = 'romance'
SCF = 'Science-Fiction'


class Book(models.Model):
    GENRE = (
        (POETRY, 'poetry'),
        (ROMANCE, 'romance'),
        (SCF, 'Science-Fiction')

    )
    title = models.CharField(max_length=120)
    slug = AutoSlugField(populate_from='title',
                         unique=True,
                         )
    author = models.ForeignKey('Author', on_delete=models.CASCADE, related_name='books')
    genre = models.CharField(max_length=120, choices=GENRE)
    price = models.DecimalField(decimal_places=2, max_digits=5)
    isbn = models.CharField(max_length=120)
    sale = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.title} by {self.author} for ${self.price}'


class Author(models.Model):
    name = models.CharField(max_length=250)

    def __str__(self):
        return self.name
