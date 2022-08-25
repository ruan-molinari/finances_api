from django.db import models

class Category(models.IntegerChoices):
    OTHER = 0, 'Other'
    FOOD = 1, 'Food'
    HEALTH = 2, 'Health'
    DWELLING = 3, 'Dwelling'
    TRANSPORTATION = 4, 'Transportation'
    EDUCATION = 5, 'Education'
    ENTERTAINMENT = 6, 'Enterprise'
    UNEXPECTED = 7, 'Unexpected'

# Create your models here.
class Income(models.Model):
    description = models.CharField(max_length=255)
    value = models.DecimalField(max_digits=19, decimal_places=2)
    date = models.DateField()

    def __str__(self) -> str:
        return self.description

class Expense(models.Model):
    description = models.CharField(max_length=255)
    value = models.DecimalField(max_digits=19, decimal_places=2)
    date = models.DateField()
    category = models.IntegerField(max_length=1, choices=Category.choices, default=0)

    def __str__(self) -> str:
        return self.description
