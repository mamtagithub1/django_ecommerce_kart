from django.http import HttpResponse
from django.shortcuts import render
from store.models import Product


def home(requests):
    # query
    products = Product.objects.all().filter(is_available=True).order_by('created_date')
    context = {
        'products': products,
        
    }
    # return HttpResponse('HomePage is Here!! ')
    return render(requests,'home.html',context)