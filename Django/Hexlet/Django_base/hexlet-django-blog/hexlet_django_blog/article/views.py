from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.views import View
from .forms import ArticleForm
from .models import Article, ArticleComment


class IndexView(View):
    def get(self, request, *args, **kwargs):
        articles = Article.objects.all()[:15]
        return render(request, 'articles/index.html', context={'articles': articles})


class ArticleView(View):
    def get(self, request, *args, **kwargs):
        article = get_object_or_404(Article, id=kwargs['id'])
        return render(request, 'articles/show.html', context={'article': article})


class ArticleCreateView(View):
    template_name = 'articles/create.html'

    def get(self, request, *args, **kwargs):
        form = ArticleForm()
        return render(request, self.template_name, context={'form': form})
    
    def post(self, request, *args, **kwargs):
        form = ArticleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
        return render(request, self.template_name, context={'form': form})
        





# class ArticleComentsView(View):
#     def get(self, request, *args, **kwargs):
#         comment = ge

# class ArticleHomeView(View):
#     def get(self, request, *args, **kwargs):
#         return HttpResponse("article ArticleHomeView 2")


def index(request, tags, article_id):
    return HttpResponse(f'Статья номер {article_id}. Тег {tags}')


# class CommentArticleView(View):

#     def post(self, request, *args, **kwargs):
#         form = CommentArticleForm(request.POST)
#         if form.is_valid():
#             comment = ArticleComment(
#                 content=form.cleaned_data[
#                     'content'
#                 ]
#             )
#             comment.save()

#     def get(self, request, *args, **kwargs):
#         form = CommentArticleForm()
#         return render(
#             request, 'articles/comment.html', {'form': form}
#         )
