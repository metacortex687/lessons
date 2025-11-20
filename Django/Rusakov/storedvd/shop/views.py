from django.shortcuts import render
from django.http import HttpResponse

from .models import Section, Product


def index(request):
    section = Section.objects.all().order_by("title")
    products = Product.objects.all().order_by(get_order_by_price(request))[:8]
    return render(
        request, "index.html", context={"sections": section, "products": products}
    )

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