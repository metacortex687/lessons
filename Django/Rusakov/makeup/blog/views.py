from typing import Any
from django.shortcuts import render, get_object_or_404
from django.db.models import Count, Q
from django.views import generic
from django.http.response import HttpResponse, HttpResponseRedirect
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.urls import reverse

from .models import Image, Comment, Article
import datetime
from .forms import SearchForm, FeedbackForm


def index(request):
    images = Image.objects.all()

    return render(
        request,
        'index.html',
        context={
            'images': images,
        },
    )


def trim_text(text: str, limit):
    if len(text) < limit:
        return text

    cut_pos = text.rfind(' ', 0, limit)
    return f'{text[:cut_pos]}...'


def about(request):
    return render(request, 'about.html')


def contact(request):
    return render(request, 'contact.html', {'form': FeedbackForm()})


def articles(request):
    articles_all = Article.objects.all().order_by('-date')
    images = Image.objects.all()[:9]

    return render(
        request,
        'articles.html',
        context={
            'articles': articles_all[:3].annotate(comment_count=Count('comment')),
            'archive_dates': sorted_list_archeve_dates(articles_all),
            'images': images,
        },
    )


def sorted_list_archeve_dates(articles_all):
    archive_dates = set()
    for article in articles_all:
        archive_dates.add(datetime.date(article.date.year, article.date.month, 1))
    archive_dates = list(archive_dates)
    archive_dates = sorted(archive_dates)
    return archive_dates


def archive(request, year, month):
    articles_all = Article.objects.all()
    images = Image.objects.all()[:9]

    return render(
        request,
        'archive.html',
        context={
            'articles': articles_all.filter(date__year=year, date__month=month)
            .order_by('-date')
            .annotate(comment_count=Count('comment')),
            'archive_dates': sorted_list_archeve_dates(articles_all),
            'current_archive_date': datetime.date(year, month, 1),
            'images': images,
        },
    )


def single(request, pk):
    articles_all = Article.objects.all()
    article = get_object_or_404(Article, pk=pk)

    if request.POST:
        username = request.POST.get('username', '')
        email = request.POST.get('email', '')
        comment = request.POST.get('comment', '')

        if username and email and comment:
            request.session['username'] = username
            request.session['email'] = email

            Comment.objects.create(
                article=article, author=username, email=email, content=comment
            )
            return HttpResponseRedirect(reverse('single', args=[pk]))

    return render(
        request,
        'single.html',
        {
            'comments': article.comment_set.all(),
            'archive_dates': sorted_list_archeve_dates(articles_all),
            'images': Image.objects.all()[:9],
            'article': article,
        },
    )


def search(request):
    images = Image.objects.all()[:9]

    search_form = SearchForm(request.GET)

    if search_form.is_valid():
        q = search_form.cleaned_data['q']
        articles = Article.objects.filter(
            Q(title__icontains=q)
            | Q(subtitle__icontains=q)
            | Q(content__icontains=q)
            | Q(author__username__icontains=q)
            | Q(author__first_name__icontains=q)
            | Q(author__last_name__icontains=q)
        )

        page = request.GET.get('page', 1)
        paginator = Paginator(articles, 5)
        try:
            articles = paginator.page(page)
        except PageNotAnInteger:
            articles = paginator.page(1)
        except EmptyPage:
            articles = paginator.page(paginator.num_pages)

    return render(
        request,
        'search.html',
        context={
            'articles': articles,
            'images': images,
            'q': q,
        },
    )
