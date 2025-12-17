from typing import Any
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.views import generic
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.urls import reverse

from .models import Section, Product, Discount, Order, OrderLine
from .forms import SearchForm, OrderModelForm
from django.db.models import Q
from django.contrib.auth.models import User, Group
from django.contrib.auth.decorators import login_required
from django.template.loader import get_template
from django.core.mail import EmailMultiAlternatives
from django.utils.crypto import get_random_string


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


def order(request):
    cart_info = request.session.get('cart_info')
    if not cart_info:
        raise Http404

    if request.method == 'POST':
        form = OrderModelForm(request.POST)
        if form.is_valid():
            order_obj = Order()
            order_obj.need_delivery = form.cleaned_data['delivery'] == 1
            discount_code = request.session.get('discount')
            if discount_code:
                try:
                    order_obj.discount = Discount.objects.get(code__exact=discount_code)
                except Discount.DoesNotExist:
                    pass
            order_obj.name = form.cleaned_data['name']
            order_obj.phone = form.cleaned_data['phone']
            order_obj.email = form.cleaned_data['email']
            order_obj.adress = form.cleaned_data['adress']
            order_obj.notice = form.cleaned_data['notice']
            order_obj.save()
            add_order_lines(request, order_obj)
            add_user(form.cleaned_data['name'], form.cleaned_data['email'])
            return HttpResponseRedirect(reverse('addorder'))

        return render(request, 'order.html', {'form': form})

    return render(request, 'order.html', {'form': OrderModelForm()})


def add_order_lines(request, order_obj):
    cart_info = request.session.get('cart_info', {})
    for key in cart_info:
        order_line = OrderLine()
        order_line.order = order_obj
        order_line.product = get_object_or_404(Product, pk=key)
        order_line.price = order_line.product.price
        order_line.count = cart_info[key]
        order_line.save()
    del request.session['cart_info']

    products = []
    if cart_info:
        for product_id in cart_info:
            try:
                product = Product.objects.get(pk=product_id)
                product.count = cart_info[product_id]
                products.append(product)
            except Product.DoesNotExist:
                raise Http404()


def addorder(request):
    return render(request, 'addorder.html')


def add_user(name, email):
    if (
        User.objects.filter(email=email).exists()
        or User.objects.filter(username=email).exists()
    ):
        return
    password = get_random_string(5)
    user = User.objects.create_user(email, email, password)
    user.first_name = name
    user.groups.add(Group.objects.get(name='Клиенты'))
    user.save()

    text = get_template('registration/registration_email.html')
    html = get_template('registration/registration_email.html')

    context = {'username': email, 'password': password}
    subject = 'Регистрация'
    from_email = 'from@storedvd.ru'

    text_content = text.render(context=context)
    html_content = html.render(context=context)
    msg = EmailMultiAlternatives(subject, text_content, from_email, [email])
    msg.attach_alternative(html_content, 'text/html')
    msg.send()

@login_required
def orders(request):
    user_orders = Order.objects.filter(email__exact=request.user.email)
    return render(request,'orders.html', {'orders':user_orders})