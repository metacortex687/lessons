from .models import Section
from .forms import SearchForm


def add_default_data(request):
    return {
        'sections': Section.objects.all().order_by('title'),
        'search_form': SearchForm(),
    }
