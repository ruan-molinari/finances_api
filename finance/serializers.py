from dataclasses import field
from rest_framework import serializers
from .models import Income, Expense

class IncomeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Income
        fields = ['id', 'description', 'value', 'date']

class ExpenseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Expense
        fields = ['id', 'description', 'value', 'date', 'category']
