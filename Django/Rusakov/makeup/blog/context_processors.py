from .models import Comment, Article
from .forms import SearchForm


def add_default_data(request):
    last_comments = Comment.objects.all()[:3]
    last_articles = Article.objects.all().order_by('-date')[:3]

    username = request.session.get('username', '')
    email = request.session.get('email', '')

    return {
        'last_comments': last_comments,
        'last_articles': last_articles,
        'search_form': SearchForm(),
        'username': username,
        'email': email,
    }
