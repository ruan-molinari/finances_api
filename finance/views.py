from django.db.models import Sum
from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Income, Expense, Category
from .serializers import IncomeSerializer, ExpenseSerializer

CATEGORIES_VALUES = [x[0] for x in Category.choices]

class IncomeViewSet(viewsets.ModelViewSet):
    """
    Income view set
    """
    queryset = Income.objects.all()
    serializer_class = IncomeSerializer
    # permission_classes = [IsAccountAdminOrReadOnly]

class ExpenseViewSet(viewsets.ModelViewSet):
    """
    Expense view set
    """
    queryset = Expense.objects.all()
    serializer_class = ExpenseSerializer

class SummaryView(APIView):
    """
    Summary by year or month
    """
    def get(self, request, year, month=None):
        qs_income = Income.objects.filter(date__year=year)
        qs_expenses = Expense.objects.filter(date__year=year)
        
        if month:
            qs_income = qs_income.filter(date__month=month)
            qs_expenses = qs_expenses.filter(date__month=month)

        total_income = qs_income.aggregate(Sum('value'))['value__sum'] or 0
        total_expenses = qs_expenses.aggregate(Sum('value'))['value__sum'] or 0

        balance = total_income - total_expenses

        total_expenses_by_category = [{'category': x[0], 'total_expenses': qs_expenses.filter(category=x[0]).aggregate(Sum('value'))['value__sum'] or 0} for x in Category.choices]

        return Response({
            'total_income': total_income,
            'total_expenses': total_expenses,
            'balance': balance,
            'total_expenses_by_category': total_expenses_by_category
        })
