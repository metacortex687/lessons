from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

from .models import Section, Product


def index(request):
    products = Product.objects.all().order_by(get_order_by_price(request))[:8]
    return render(request, 'index.html', context={'products': products})


def get_order_by_price(request):
    order_by = ''
    if request.GET.__contains__('sort') and request.GET.__contains__('up'):
        sort = request.GET['sort']
        up = request.GET['up']
        if sort == 'price' or sort == 'title':
            if up == '0':
                order_by = '-'
            order_by += sort
    if not order_by:
        order_by = '-date'

    return order_by


def delivery(request):
    return render(request, 'delivery.html')


def contacts(request):
    return render(request, 'contacts.html')


def section(request, id):
    obj = get_object_or_404(Section, pk=id)
    products = Product.objects.filter(section__exact=obj).order_by(
        get_order_by_price(request)
    )
    return render(
        request, 'section.html', context={'section': obj, 'products': products}
    )
