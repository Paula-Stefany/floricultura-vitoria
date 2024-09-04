from django.http import HttpResponse
from floriCultura.models.Category import Category
from django.shortcuts import render
from floriCultura.models.Product import Product


def home_view(request, category_id = None):

    categorys = Category.objects.all()

    if category_id is not None:
        products = Product.objects.filter(category_id=category_id)

    else:
        products = Product.objects.all()

    context = {
        'categorys': categorys,
        'products': products
    }

    return render(request, template_name="EcommerceScreen.html", context=context)
