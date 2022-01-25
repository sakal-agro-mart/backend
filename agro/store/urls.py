from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views


urlpatterns = [
    path('categories/', views.CategoryList.as_view()),
    path('products/search/', views.ProductSearch.as_view()),
    path('products/featured/', views.FeaturedProducts.as_view()),
    path('products/recent/', views.RecentProducts.as_view()),
    path('carousels/', views.CarouselList.as_view())
]

urlpatterns = format_suffix_patterns(urlpatterns)
