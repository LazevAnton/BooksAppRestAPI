from django.db import models


class BooksInfo(models.Model):
    book_name = models.CharField(max_length=250, blank=False)
    book_year = models.DateField(blank=False, max_length=4)
    book_price = models.DecimalField(max_digits=7, decimal_places=2)

    def __str__(self):
        return f'{self.book_name} - {self.book_price}'