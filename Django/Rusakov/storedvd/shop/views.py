from typing import Any
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.views import generic
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

from .models import Section, Product
from .forms import SearchForm
from django.db.models import Q


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


class ProdactDetailView(generic.DetailView):
    model = Product
    template_name = 'product_detail.html'

    def get_context_data(self, **kwargs) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['products'] = Product.objects.filter(
            section__exact=self.get_object().section
        ).exclude(id=self.get_object().id)
        return context


def search(request):
    search_form = SearchForm(request.GET)

    if search_form.is_valid():
        q = search_form.cleaned_data['q']
        products = Product.objects.filter(
            Q(title__icontains=q)
            | Q(country__icontains=q)
            | Q(director__icontains=q)
            | Q(cast__icontains=q)
            | Q(description__icontains=q)
        )
        page = request.GET.get('page', 1)
        paginator = Paginator(products, 2)
        try:
            products = paginator.page(page)
        except PageNotAnInteger:
            products = paginator.page(1)
        except EmptyPage:
            products = paginator.page(paginator.num_pages)

    return render(request, 'search.html', {'products': products, 'q': q})
