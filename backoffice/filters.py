import django_filters
from .models import Work


class WorkFilterSet(django_filters.FilterSet):
    class Meta:
        model = Work
        fields = ['designer', 'category', 'subjects', 'name_he',
                  'of_collections', 'publish_year', 'description_he']
