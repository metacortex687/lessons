from django.shortcuts import render

from .models import Image, Comment, Article


def index(request):
    images = Image.objects.all()
    trim_comments = map(lambda x: trim_text(x.content, 150), Comment.objects.all()[:3])
    articles = Article.objects.all().order_by("-date")[:3]

    return render(
        request,
        "index.html",
        context={"images": images, "trim_comments": trim_comments, "articles": articles},
    )


def trim_text(text: str, limit):
    if len(text) < limit:
        return text

    cut_pos = text.rfind(" ", 0, limit)
    return f"{text[:cut_pos]}..."
