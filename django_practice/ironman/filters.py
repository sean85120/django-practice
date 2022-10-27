from django_filters import FilterSet, NumberFilter, CharFilter, BooleanFilter
from .models import People

class PeopleFilterSet(FilterSet):
    name = CharFilter(field_name='name', max_length=100)
    age_from = NumberFilter(field_name='age', lookup_expr='gte')
    age_to = NumberFilter(field_name='age', lookup_expr='lte')
    power = BooleanFilter(field_name='power')
    

    class Meta:
        model = People
        fields = ('name', 'age_from', 'age_to', 'power')