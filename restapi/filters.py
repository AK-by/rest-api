from django_filters import rest_framework as filters
from . models import SimpleMessages


class MessageFilter(filters.FilterSet):
    title = filters.CharFilter(field_name="title", lookup_expr="icontains")
    message = filters.CharFilter(field_name="message", lookup_expr="icontains")
    created = filters.DateRangeFilter(field_name="created")
    title_and_message = filters.CharFilter(method="filter_by_title_and_message")

    # author = filters.ModelChoiceFilter(
    # )
    # author = filters.ModelMultipleChoiceFilter(
    #     queryset=Author.objects.all(),
    #     field_name="author",
    #     to_field_name="id",
    #     lookup_expr="exact",
    # )

    def filter_by_title_and_message(self, queryset, name, value):
        parts = value.split(",")
        title = parts[0]
        message = parts[1]
        if title:
            queryset = queryset.filter(title__icontains=title)
        if message:
            queryset = queryset.filter(message__icontains=message)
        return queryset

    class Meta:
        model = SimpleMessages
        fields = ("title", "message", )
