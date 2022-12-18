from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import *

urlpatterns = format_suffix_patterns([
    path('products/', ProductsViewSet.as_view({'get': 'list'})),
    path('products/<int:pk>/', ProductsViewSet.as_view({'get': 'retrieve'})),
    path('cart/', CartView.as_view()),
    path('review/', ReviewCreateViewSet.as_view({'post': 'create'})),
    path('rating/', AddStarRatingViewSet.as_view({'post': 'create'})),
    path('category/', CategoryList.as_view())
])