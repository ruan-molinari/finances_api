from django.shortcuts import render
from rest_framework import viewsets, filters
from .models import Income, Expense
from .serializers import IncomeSerializer, ExpenseSerializer

# Create your views here.
class IncomeViewSet(viewsets.ModelViewSet):
    queryset = Income.objects.all()
    serializer_class = IncomeSerializer
    search_fields = ['description', 'date']
    # permission_classes = [IsAccountAdminOrReadOnly]

class ExpenseViewSet(viewsets.ModelViewSet):
    queryset = Expense.objects.all()
    serializer_class = ExpenseSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['description', 'date', 'category']
