from django.views.generic import ListView, DetailView

from .models import Category, Product


class CategoryListView(ListView):
    model = Category # Category.object.all()
    template_name = 'home.html'
    context_object_name = 'categories'


class ProductListView(ListView):
    model = Product # Product.object.all()
    template_name = 'product_list.html'
    context_object_name = 'products'

    def get_queryset(self):
        queryset = super().get_queryset()
        slug = self.kwargs.get('slug')
        queryset = queryset.filter(category__slug=slug)
        return queryset


class ProductDetailView(DetailView):
    model = Product
    template_name = 'detail.html'
    context_object_name = 'product'
    pk_url_kwarg = 'product_id'

