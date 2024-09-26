import django_filters
from .models import Book
from lists.models import ListItem

class GenreFilter(django_filters.FilterSet):
    genre = django_filters.CharFilter(field_name='genre__name', lookup_expr='icontains')

    class Meta:
        model = Book
        fields = ['genre']


class GenreFilterForListItem(django_filters.FilterSet):
    genre = django_filters.CharFilter(field_name='book__genre__name', lookup_expr='icontains')

    class Meta:
        model = ListItem
        fields = ['genre']
