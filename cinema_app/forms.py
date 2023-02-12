from django import forms
from .models import Category


class AddCategoryForm(forms.Form):

    class Meta:
        model = Category
        fields = ('category_name', 'slug')