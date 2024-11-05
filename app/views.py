from django.shortcuts import render
from products.models import Product, Category


def index(request):
    products = Product.objects.all()
    categories = Category.objects.all()
    context = {
        'products': products,
        'categories': categories
    }
    return render(request, 'index.html', context=context)

def contact(request):
    return render(request, 'contact.html')