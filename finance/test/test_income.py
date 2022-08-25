from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIClient
from finance.models import Income
from .factory import IncomeFactory
from faker import Faker

class IncomeTestCase(APITestCase):

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.income_object = IncomeFactory.build()
        cls.income_saved = IncomeFactory.create()
        cls.client = APIClient()
        cls.url = reverse('income-list')
        cls.faker_obj = Faker()

    def test_if_data_is_correct_then_register(self):
        # Prepare data
        income_dict = {
            'description': self.income_object.description,
            'value': self.income_object.value,
            'date': self.income_object.date,
        }
        # Make request
        response = self.client.post(self.url, income_dict)
        # Check response
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Income.objects.count(), 2)
        # Check database
        new_income_registry = Income.objects.get(description=self.income_object.description)
        self.assertEqual(new_income_registry.value, self.income_object.value)
        self.assertEqual(new_income_registry.date, self.income_object.date)
