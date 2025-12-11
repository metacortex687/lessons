from .models import Section, Product
from .forms import SearchForm


def add_default_data(request):
    count_in_cart = 0
    sum_in_cart = 0
    cart_info = request.session.get('cart_info', {})
    for key in cart_info:
        count_in_cart += cart_info[key]
        sum_product = Product.objects.get(pk=key).price * cart_info[key]
        sum_in_cart += sum_product

    return {
        'sections': Section.objects.all().order_by('title'),
        'search_form': SearchForm(),
        'count_in_cart': count_in_cart,
        'sum_in_cart': sum_in_cart,
    }
