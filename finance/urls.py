from django.urls import path, include
from rest_framework import routers
from .views import IncomeViewSet, ExpenseViewSet

router = routers.DefaultRouter()
router.register('income', IncomeViewSet, basename='income')
router.register('expense', ExpenseViewSet, basename='expense')

urlpatterns = [
    path('', include(router.urls))
]
