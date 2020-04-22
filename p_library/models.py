from django.db import models
from decimal import Decimal  
  
  
class Author(models.Model):  
    full_name = models.CharField(max_length=30)
    birth_year = models.SmallIntegerField()  
    country = models.CharField(max_length=2)
    
    def __str__(self):
        return self.full_name


class Publisher(models.Model):  
    name = models.TextField()
    address = models.CharField(max_length=50, null=True, blank=True)
    city = models.CharField(max_length=60, null=True, blank=True)
    state_province = models.CharField(max_length=30, null=True, blank=True)
    country = models.CharField(max_length=50, null=True, blank=True)
    website = models.URLField(null=True, blank=True)

    def __str__(self):
        return self.name  


class Book(models.Model):  
    ISBN = models.CharField(max_length=13)  
    title = models.TextField()  
    description = models.TextField()  
    year_release = models.SmallIntegerField()  
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    publisher = models.ForeignKey(Publisher, null=True, on_delete=models.CASCADE, blank=True, related_name='books')
    copy_count = models.SmallIntegerField(default=0)
    price = models.DecimalField(max_digits=6, decimal_places=2, default=Decimal('0000.00'))
    cover = models.ImageField(upload_to='covers', blank=True)

    def __str__(self):
        return self.title


class Friend(models.Model):
    name = models.CharField(max_length=30)
    phone = models.CharField(max_length=15, null=True, blank=True)

    def __str__(self):
        return self.name


class LendedBooks(models.Model):
    friend = models.ForeignKey(Friend, on_delete=models.CASCADE, related_name='friends')
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='books')
    date_lend_in = models.DateField(auto_now=False, auto_now_add=True)
    date_lend_out = models.DateField(auto_now=False, auto_now_add=False, blank=True, editable=True, null=True)

    def __str__(self):
        return self.book.title

    class Meta:
        verbose_name = 'Одолженная книга'
        verbose_name_plural = 'Одолженные книги'



