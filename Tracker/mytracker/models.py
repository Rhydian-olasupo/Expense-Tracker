from django.db import models
from django.utils import timezone

# Create your models here.

'''SELECT_BOOK_CATEGORY = [
    ("Business Analytics","Business Analytics"),
    ("Deep Learning","Deep Learning"),
    ("Visualization","Visualization"),
    ("Data Science","Data Science"),
    ("Data Ethics","Data Ethics"),
    ("Math","Math"),
    ("NLP","NLP"),
    ("Statistics","Statistics"),
    ("SQL","SQL"),
    ("R studio","R studio"),
    ('Pyhton',"Python"),]'''

class Category(models.Model):
    category = models.CharField(max_length=50)
    def __str__(self) -> str:
        return self.category

class Books(models.Model):
    title = models.CharField(max_length=255)
    subtitle = models.TextField(max_length=500)
    authors = models.CharField(max_length=255)
    publisher = models.CharField(max_length=255)
    published_date = models.DateField(default=timezone.now)
    category = models.ForeignKey(Category,on_delete=models.PROTECT)
    distribution_expense = models.DecimalField(max_digits=6,decimal_places=2)

    def __str__(self) -> str:
        return self.title