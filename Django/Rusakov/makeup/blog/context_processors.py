from .models import Comment, Article


def add_default_data(request):
    last_comments = Comment.objects.all()[:3]
    last_articles = Article.objects.all().order_by('-date')[:3]

    return {'last_comments': last_comments, 'last_articles': last_articles}
