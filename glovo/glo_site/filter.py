from django_filters.rest_framework import FilterSet
from .models import Food


class FoodFilter(FilterSet):
    class Meta:
        model = Food
        fields = {
            'resto_name': ['exact'],
            'price': ['gt', 'lt'],
            'category': ['exact'],
        }