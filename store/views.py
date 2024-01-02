from django.shortcuts import render, get_object_or_404, redirect
from store.models import Product
from category.models import Category
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator

# Create your views here.
def store(requests, category_slug=None):
    categories = None
    products = None
    if category_slug != None:
        categories = get_object_or_404(Category, slug_name=category_slug)
        products = Product.objects.filter(category=categories, is_available=True)
        paginator = Paginator(products, 1)
        page = requests.GET.get('page')
        paged_products = paginator.get_page(page)
        product_count = products.count()
    else:
        products = Product.objects.all().filter(is_available=True) #.order_by('id')
        paginator = Paginator(products, 3)
        page = requests.GET.get('page')
        paged_products = paginator.get_page(page)
        product_count = products.count()
    context = {
        'products': products,
        'product_count': product_count,
        
    }
    return render(requests,'store/store.html',context)

def product_detail(request, category_slug, product_slug):
    try:
        single_product=Product.objects.get(category__slug_name=category_slug,slug=product_slug)
    except Exception as e:
        raise e
    context={
        'single_product':single_product
    }
    return render(request, 'store/product_detail.html',context)




