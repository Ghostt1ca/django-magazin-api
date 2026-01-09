from django.urls import path
from .views import ProdusListCreate, ProdusDetail

urlpatterns = [
    path('produse/', ProdusListCreate.as_view(), name='produse-list'),
    path('produs/<int:pk>/', ProdusDetail.as_view(), name='produs-detail')
]