from django.shortcuts import render
from .models import Product


def products_list(request, *args, **kwargs):
    if request.method == 'GET':
        products = Product.objects.all()
        print(products)
        context = {'products': products}
        return render(request, 'app_food/index.html',
                      context=context
                      )
