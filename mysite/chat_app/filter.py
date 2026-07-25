from .models import UserProfile
from django_filters.rest_framework import FilterSet


class UserFilter(FilterSet):
    class Meta:
        model = UserProfile
        fields = {
            'username': ['exact'],
            'bio': ['exact']
        }