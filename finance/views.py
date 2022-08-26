from django.db.models import Sum
from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Income, Expense
from .serializers import IncomeSerializer, ExpenseSerializer

# Create your views here.
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

class MothSummaryView(APIView):
    """
    Month summary by month
    """
    def get(self, year, month):
        total_month_income = Income.objects.filter(date__year=year, date__month=month).aggregate(Sum('value'))['value__sum'] or 0
        total_month_expenses = Expense.objects.filter(date__year=year, date__month=month).aggregate(Sum('value'))['value__sum'] or 0



        
        
