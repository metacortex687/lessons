from django.shortcuts import render
from django.http import HttpResponse
from django.views import View


# class ArticleHomeView(View):
#     def get(self, request, *args, **kwargs):
#         return HttpResponse("article ArticleHomeView 2")

def index(request, tags, article_id):
    return HttpResponse(f"Статья номер {article_id}. Тег {tags}")





