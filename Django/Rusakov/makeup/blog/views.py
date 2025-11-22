from typing import Set
from django.shortcuts import render
from django.db.models import Count

from .models import Image, Comment, Article
import datetime
import random


def index(request):
    images = Image.objects.all()
    trim_comments = map(lambda x: trim_text(x.content, 150), Comment.objects.all()[:3])
    articles = Article.objects.all().order_by('-date')[:3]

    return render(
        request,
        'index.html',
        context={
            'images': images,
            'trim_comments': trim_comments,
            'articles': articles,
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
    return render(request, 'contact.html')


def articles(request):
    articles_all = Article.objects.all().order_by('-date')
    images = Image.objects.all()[:9]

    return render(
        request,
        'articles.html',
        context={
            'articles': articles_all[:3]            
            .annotate(comment_count=Count('comment')),
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
    print(archive_dates)
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
