from django.urls import path
from .views import (CategoryListView, category_view,
                     product_detail, AddCategoryView,
                     UpdateCategoryView)

urlpatterns = [
    path('categories/', CategoryListView.as_view(), name='categories'),
    path('category/<slug:slug>/', category_view, name='category'),
    path('product/<int:pk>', product_detail, name='product'),
    path('add_category/', AddCategoryView.as_view(), name='add_category'),
    path('edit_category/<slug:slug>/',UpdateCategoryView.as_view(), name='edit_category'),
    
]
