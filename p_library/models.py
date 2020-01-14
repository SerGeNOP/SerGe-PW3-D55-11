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

    def __str__(self):
        return self.title
