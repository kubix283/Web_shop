from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView
from .models import Category, Product

class CategoryListView(ListView):
    model = Category
    template_name = 'category_list.html'
    context_object_name = 'categories'

    def get_queryset(self):
        return Category.objects.all().order_by('category_name')



def category_view(request, slug):
    category = Category.objects.get(slug=slug)
    products = Product.objects.filter(categories=category).order_by('name')
    for product in products:
        product.price_brutto = product.price * (1 + product.vat)

    context = {'products': products, 'category': category}
    return render(request, 'category_detail.html', context)


def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    categories = product.categories.all()
    return render(request, 'product_detail.html', {'product': product, 'categories': categories})