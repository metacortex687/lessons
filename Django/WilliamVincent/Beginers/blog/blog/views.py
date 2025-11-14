from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from . models import Post
from django.urls import reverse_lazy

class BlogListView(ListView):
    model = Post
    template_name = 'home.html'

class BlogDetailedView(DetailView):
    model = Post
    template_name = 'post_detailed.html'
    context_object_name = 'anything_you_want'

class BlogDeleteView(DeleteView):
    model = Post
    template_name = 'post_delete.html'
    success_url = reverse_lazy('home')


class BlogCreateView(CreateView):
    model = Post
    template_name = 'post_new.html'
    fields = '__all__'

class BlogUpdateView(UpdateView):
    model = Post
    fields = ['title','body']
    template_name = 'post_edit.html'

