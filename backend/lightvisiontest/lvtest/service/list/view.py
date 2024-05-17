__all__ = ['GetList']

from rest_framework import serializers, generics
from lvtest.models import Image
from django_filters import rest_framework
from rest_framework.pagination import PageNumberPagination
from rest_framework import filters


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ['id', 'name', 'filetype', 'text_id']


class ImageFilter(rest_framework.FilterSet):
    class Meta:
        model = Image
        fields = ['filetype']


class StandardResultsSetPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100


class GetList(generics.ListAPIView):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer
    filter_backends = (rest_framework.DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)
    filterset_class = ImageFilter
    search_fields = ['name', 'filetype']
    ordering_fields = ['id', 'name', 'filetype']
    pagination_class = StandardResultsSetPagination
