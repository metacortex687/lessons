from typing import Any
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.views import generic
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.urls import reverse

from .models import Section, Product, Discount
from .forms import SearchForm
from django.db.models import Q


def index(request):
    result = prerender(request)
    if result:
        return result
    products = Product.objects.all().order_by(get_order_by_price(request))[:8]
    return render(request, 'index.html', context={'products': products})


def prerender(request):
    product_id = request.GET.get('add_cart')
    if product_id:
        get_object_or_404(Product, pk=product_id)
        cart_info = request.session.get('cart_info', {})
        count = cart_info.get(product_id, 0)
        count += 1
        cart_info.update({product_id: count})
        request.session['cart_info'] = cart_info
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'), '/')


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
    result = prerender(request)
    if result:
        return result

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

    def get(self, request, *args, **kwargs):
        result = prerender(request)
        if result:
            return result
        return super(ProdactDetailView, self).get(self, request, *args, **kwargs)

    def get_context_data(self, **kwargs) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['products'] = Product.objects.filter(
            section__exact=self.get_object().section
        ).exclude(id=self.get_object().id)
        return context


def search(request):
    result = prerender(request)
    if result:
        return result

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


def cart(request):
    result = update_cart_info(request)
    if result:
        return result

    cart_info = request.session.get('cart_info')
    products = []
    if cart_info:
        for product_id in cart_info:
            try:
                product = Product.objects.get(pk=product_id)
                product.count = cart_info[product_id]
                products.append(product)
            except Product.DoesNotExist:
                raise Http404()

    return render(request, 'cart.html', {'products': products})


def update_cart_info(request):
    if request.POST:
        cart_info = {}
        for param in request.POST:
            value = request.POST.get(param)
            print(param, value)
            if param.startswith('count_') and value.isnumeric():
                product_id = param.replace('count_', '')
                get_object_or_404(Product, pk=product_id)
                cart_info[product_id] = int(value)
            if param == 'discount' and value:
                try:
                    Discount.objects.get(code__exact=value)
                    request.session['discount'] = value
                except Discount.DoesNotExist:
                    request.session['discount'] = ''

        request.session['cart_info'] = cart_info

    if request.GET.get('delete_cart'):
        product_id = request.GET.get('delete_cart')
        get_object_or_404(Product, pk=product_id)
        cart_info = request.session.get('cart_info')
        current_count = cart_info.get(product_id, 0)
        if current_count <= 1:
            cart_info.pop(product_id)
        else:
            cart_info[product_id] -= 1
        request.session['cart_info'] = cart_info
        return HttpResponseRedirect(reverse('cart'))
