from django.urls import path
from .views import CategoryListView, category_view, product_detail

urlpatterns = [
    path('categories/', CategoryListView.as_view(), name='categories'),
    path('category/<slug:slug>/', category_view, name='category'),
    path('product/<int:pk>', product_detail, name='product'),
]
