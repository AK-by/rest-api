from django_filters import rest_framework as filters
from . models import SimpleMessages


class MessageFilter(filters.FilterSet):
    title = filters.CharFilter(field_name="title", lookup_expr="icontains")
    message = filters.CharFilter(field_name="message", lookup_expr="icontains")

    class Meta:
        model = SimpleMessages
        fields = ("title", "message", )
