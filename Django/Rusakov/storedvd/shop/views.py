from django.shortcuts import render
from django.http import HttpResponse

from .models import Section, Product


def index(request):
    section = Section.objects.all().order_by("title")
    products = Product.objects.all()[:8]
    return render(request, "index.html", context={"sections": section, 'products': products})
