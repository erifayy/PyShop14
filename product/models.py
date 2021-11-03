from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.enums import Choices



#TODO: Create tables Product, Category
#TODO: Notebooks --> ACER, MacBook, ASUS
#TODO: Accessories --> Earphones, PowerBank
#TODO: по 2 продукта на каждую категорию




class Category(models.Model):
    title = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(primary_key=True)
    parent = models.ForeignKey('self', blank=True, null=True, on_delete=models.CASCADE, related_name='children')

    def __str__(self) -> str:
        if self.parent:
            return f"{self.parent} --> {self.title}"
        return self.title


class Product(models.Model):
    STATUS_CHOICES = (
        ('in stock', 'In stock'), 
        ('ot of stock', 'Out of stock'),
        ('awaiting', 'Awaiting')
    )

    name = models.CharField(max_length=155)
    status = models.CharField(choices=STATUS_CHOICES, max_length=25)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    image = models.ImageField(upload_to='prod_images')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')

    def __str__(self):
        return self.name
