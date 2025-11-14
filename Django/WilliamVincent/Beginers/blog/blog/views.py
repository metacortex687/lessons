from django.views.generic import ListView, DeleteView

from . models import Post

class BlogListView(ListView):
    model = Post
    template_name = 'home.html'

class BlogDetailedView(DeleteView):
    model = Post
    template_name = 'post_detailed.html'
    context_object_name = 'anything_you_want'
