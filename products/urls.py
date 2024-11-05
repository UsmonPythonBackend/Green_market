from django.urls import path
from .views import ProductsView, ProductCreateView, ProductDetailView

urlpatterns = [
    path('product/', ProductsView.as_view(), name='products-list'),
    path('product/create/', ProductCreateView.as_view(), name='products-create'),
    path('product/<int:id>/', ProductDetailView.as_view(), name='product-detail'),
]