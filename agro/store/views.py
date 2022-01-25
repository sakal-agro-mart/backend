from django.shortcuts import render
from rest_framework import generics

from .serializers import CarouselSerializer, CategorySerializer, ProductSerializer
from .models import Carousel, Category, Product
from .paginations import CustomPagination
from .search_filters import CustomSearchFilter


# Create your views here.

class CategoryList(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    pagination_class = CustomPagination

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class ProductSearch(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    pagination_class = CustomPagination
    filter_backends = [CustomSearchFilter]

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class FeaturedProducts(generics.ListAPIView):
    queryset = Product.objects.filter(featured=True)
    serializer_class = ProductSerializer
    pagination_class = CustomPagination

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class RecentProducts(generics.ListAPIView):
    queryset = Product.objects.filter(recent=True)

    serializer_class = ProductSerializer
    pagination_class = CustomPagination

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class CarouselList(generics.ListAPIView):
    queryset = Carousel.objects.all()

    serializer_class = CarouselSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
