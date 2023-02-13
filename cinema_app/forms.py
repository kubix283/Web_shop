from django import forms
from .models import Category, Product


class AddCategoryForm(forms.Form):

    class Meta:
        model = Category
        fields = ('category_name', 'slug')


class AddProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = ('__all__')