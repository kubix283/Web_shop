from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from .forms import AddCategoryForm, AddProductForm
from django.views.generic import (ListView, CreateView,
                                   UpdateView, DeleteView,
                                   TemplateView)
from .models import Category, Product

class HomeView(TemplateView):
    template_name = 'index.html'



class CategoryListView(ListView):
    model = Category
    template_name = 'category/category_list.html'
    context_object_name = 'categories'

    def get_queryset(self):
        return Category.objects.all().order_by('category_name')



def category_view(request, slug):
    category = Category.objects.get(slug=slug)
    products = Product.objects.filter(categories=category).order_by('name')
    for product in products:
        product.price_brutto = product.price * (1 + product.vat)

    context = {'products': products, 'category': category}
    return render(request, 'category/category_detail.html', context)


def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    categories = product.categories.all()
    return render(request, 'product/product_detail.html', {'product': product, 'categories': categories})



class AddCategoryView(CreateView):
    model = Category
    fields = ('category_name', 'slug')
    template_name = 'category/add_category.html'
    success_url = reverse_lazy('categories')


class UpdateCategoryView(UpdateView):
    model = Category
    template_name = 'category/update_category.html'
    fields = ('__all__')
    success_url = reverse_lazy('categories')


class ProductListView(ListView):
    model = Product
    template_name = 'product/product_list.html'
    context_object_name = 'products'

class ProductUpdateView(UpdateView):
    model = Product
    template_name = 'product/product_update.html'
    form_class = AddProductForm
    success_url = reverse_lazy('product_list')

class AddProductView(CreateView):
    model = Product
    form_class = AddProductForm
    template_name = 'product/add_product.html'
    success_url = reverse_lazy('product_list')

class ProductDeleteView(DeleteView):
    
    model = Product
    template_name = 'product/product_delete.html'
    context_object_name = 'product'
    success_url = reverse_lazy('product_list')

