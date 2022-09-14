from django_filters import rest_framework as filters
from django_filters import DateTimeFromToRangeFilter, DateTimeFilter, ModelChoiceFilter, DateRangeFilter
from advertisements.models import Advertisement


class AdvertisementFilter(filters.FilterSet):
    """Фильтры для объявлений."""

    # TODO: задайте требуемые фильтры

    created_at = DateRangeFilter(name='created_at')

    class Meta:
        model = Advertisement
        fields = ['created_at']
