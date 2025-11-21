from .models import Section


def add_default_data(request):
    return {'sections': Section.objects.all().order_by('title')}
