from django.db import models

class Category(models.Choices):
    OTHER = 'Other'
    FOOD = 'Food'
    HEALTH = 'Health'
    DWELLING = 'Dwelling'
    TRANSPORTATION = 'Transportation'
    EDUCATION = 'Education'
    ENTERTAINMENT = 'Entertainment'
    UNEXPECTED = 'Unexpected'

# Create your models here.
class Income(models.Model):
    description = models.CharField(max_length=255)
    value = models.DecimalField(max_digits=19, decimal_places=2)
    date = models.DateField()

    def __str__(self) -> str:
        return self.description

class Expense(models.Model):
    description = models.CharField(max_length=255)
    value = models.DecimalField(max_digits=32, decimal_places=2)
    date = models.DateField()
    category = models.CharField(max_length=128, choices=Category.choices, default=Category.OTHER)

    def __str__(self) -> str:
        return self.description
