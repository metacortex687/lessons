from django.shortcuts import render, redirect
from django.views.generic.base import TemplateView
from django.urls import reverse

class HomePageView(TemplateView):
    template_name = "index.html"

    def get(self, request):
        return redirect(reverse('article',args=['python',42]))

    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        context['who'] = "World 3"

        return context
        

# def index(request):
#     return render(
#         request,
#         "index.html",
#         context={
#             "who": "World 2",
#         }
#     )


def about(reques):
    tags = ["обучение","программирование","python","oop"]
    return render(
        reques,
        "about.html",
        context={"tags": tags}
    )