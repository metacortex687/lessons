from django.shortcuts import render
from django.http import HttpResponse

from .models import Section


def index(request):
    section = Section.objects.all().order_by("title")
    return render(request, "index.html", context={"sections": section})
