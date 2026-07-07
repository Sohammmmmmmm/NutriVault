from django.db import models

# Create your models here.

class Brand(models.Model):
    Name = models.CharField(max_length=100)
    Description = models.TextField()

    def __str__(self):
        return self.Name
    
class Category(models.Model):
    Name = models.CharField(max_length=100)
    Description = models.TextField()

    def __str__(self):
        return self.Name

class Product(models.Model):
    Name = models.CharField(max_length=100)
    Description = models.TextField()
    Price = models.DecimalField(max_digits=10, decimal_places=2)
    Category = models.ForeignKey(Category, on_delete=models.CASCADE)
    

    def __str__(self):
        return self.Name