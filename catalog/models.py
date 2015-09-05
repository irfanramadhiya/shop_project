from django.db import models

# Create your models here.
class Brand(models.Model):
    name = models.CharField(max_length=200)

class Product(models.Model):
    CATEGORIES =(
        ("B", "Bed Sheet"),
        ("T", "Table Cloth"),
        ("N", "Napkins"),
        ("C", "Cushion Cover"),
    )
    SIZE =(
        ("SK", "Super King Size"),
        ("K", "King Size"),
        ("Q", "Queen Size"),
        ("S", "Single Size"),
        ("6", "For 6 Person"),
        ("8", "For 8 Person"),
        ("10", "For 10 Person"),
        ("12", "For 12 Person"),
    )
    categories = models.CharField(max_length=200,choices=CATEGORIES)
    name = models.CharField(max_length=200)
    size = models.CharField(max_length=200,choices=SIZE)
    color = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    material = models.CharField(max_length=200)
    stock = models.IntegerField()
    description = models.TextField()
