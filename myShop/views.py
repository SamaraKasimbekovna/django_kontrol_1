from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse


from django.shortcuts import render
from .models import Category, Product

def home_view(request):
    return HttpResponse("Hello")


def categories_list(request):
    categories = Category.objects.all()
    return render(request, 'categories.html', {'categories': categories})


def products_list(request):
    products = Product.objects.all()
    return render(request, 'products.html', {'products': products})


def category_products(request, category_id):
    category = Category.objects.get(id=category_id)
    products = Product.objects.filter(category=category)

    return render(request, 'category_products.html', {
        'category': category,
        'products': products
    })

# Create your views here.
