from django.shortcuts import render


def list_products_view(request):
    pass 


def about_product_view(request):
    return render(request, template_name='AboutThePlant.html', status=200)


def product_care_view(request):
    pass 
