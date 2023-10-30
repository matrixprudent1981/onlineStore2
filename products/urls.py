from django.urls import path
from . import views

urlpatterns = [
    path('products/', views.productListView),
    path("products/<int:id>", views.productDetailView),
    path("products/create/", views.productCreateView)
]