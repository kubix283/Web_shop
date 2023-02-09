from django.shortcuts import render
from django.views.generic import ListView
from .models import Category

class CategoryListView(ListView):
    model = Category
    template_name = 'category_list.html'
    context_object_name = 'categories'

    def get_queryset(self):
        return Category.objects.all().order_by('category_name')

