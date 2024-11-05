from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.views import View
from products.forms import ProductForm
from products.models import Product
from .helpers import Pagination
from django.views.generic import ListView, DetailView
from django.contrib import messages

class ProductsView(View):
    def get(self, request, *args, **kwargs):
        products = Product.get_queryset()
        pagination = Paginator(products, 10)
        # pagination = Paginator(products, 6)
        page = int(request.GET.get('page', 1))
        pages = Pagination.page_pagination(products, 6, page)
        context = {'pages': pages, 'page': page, "previous_page": page - 1, "next_page": page + 1, "next_page2": page + 2}
        return render(request, "shop.html", context)


class ProductDetailView(View):
    def get(self, request, id):
        product = Product.objects.get(id=id)
        return render(request, "shop-detail.html", {"product": product})

class ProductCreateView(View):
    def get(self, request):
        form = ProductForm()
        return render(request, "product_create.html", {"form": form})

    def post(self, request):
        form = ProductForm(request.POST)
        if form.is_valid():
            product = form.save(commit=False)
            product.slug = product.title + "001"
            product.save()
            return redirect("products-list")

