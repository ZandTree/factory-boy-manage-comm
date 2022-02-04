from django.db import models
from django.db.models import Sum
from django.utils import timezone
from fam.models import Customer

from books.models import Book


class Purchase(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='purchases')
    books = models.ManyToManyField(Book, related_name='books_purchased')
    placed_at = models.DateTimeField(timezone.now)

    @property
    def total(self):
        total_books = self.books.all().aggregate(summ=Sum('price'))
        print('model purchase total is:', total_books)
        return total_books.get('summ', 'not found')

    def __str__(self):
        return f'{self.customer.name} bought for ${self.total}'
