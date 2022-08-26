from django.urls import path, include
from rest_framework import routers
from finance.models import Expense, Income
from .views import IncomeViewSet, ExpenseViewSet, SummaryView

router = routers.DefaultRouter()
router.register('income', IncomeViewSet, basename='income')
router.register('expenses', ExpenseViewSet, basename='expenses')

urlpatterns = [
    path('', include(router.urls)),

    path('summary/<int:year>/', SummaryView.as_view()),
    path('summary/<int:year>/<int:month>/', SummaryView.as_view()),
]
