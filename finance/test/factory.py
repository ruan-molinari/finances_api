import factory
from factory import Faker
from finance.models import Income, Expense, Category

CATEGORIES_VALUES = [x[0] for x in Category.choices]

class IncomeFactory(factory.django.DjangoModelFactory):
    
    class Meta:
        model = Income
    
    description = Faker('word')
    value = Faker('pydecimal', left_digits=4, right_digits=2, positive=True, min_value=200, max_value=9000)
    date = Faker('date_this_year')

class ExpenseFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = Expense

    description = Faker('word')
    value = Faker('pydecimal', left_digits=3, right_digits=2, positive=True, min_value=200, max_value=900)
    date = Faker('date_this_year')
    category = Faker('random_element', elements=CATEGORIES_VALUES)
