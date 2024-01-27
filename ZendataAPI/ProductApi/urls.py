from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from .views import ProductDetail, ProductList

urlpatterns = [
    path('', ProductList.as_view(), name="ProductList"),
    path('<int:pk>/', ProductDetail.as_view(), name="ProductDetail"),
]

urlpatterns = format_suffix_patterns(urlpatterns)
