from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIClient
from finance.models import Expense
from .factory import ExpenseFactory
from faker import Faker

class ExpenseTestCase(APITestCase):
    
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.expense_object = ExpenseFactory.build()
        cls.expense_saved = ExpenseFactory.create()
        cls.client = APIClient()
        cls.expense_url = reverse('expenses-list')
        cls.faker_obj = Faker()

    def test_expense_registry(self):
        # Prepare data
        expense_dict = {
            'description': self.expense_object.description,
            'value': self.expense_object.value,
            'date': self.expense_object.date,
            'category': self.expense_object.category,
        }

        # Make Request
        response = self.client.post(self.expense_url, expense_dict)
        # Check response
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Expense.objects.count(), 2),
        # Check database
        new_expense_registry = Expense.objects.get(description=self.expense_object.description)
        self.assertEqual(new_expense_registry.value, self.expense_object.value)
        self.assertEqual(new_expense_registry.date, self.expense_object.date)
        self.assertEqual(new_expense_registry.category, self.expense_object.category)
