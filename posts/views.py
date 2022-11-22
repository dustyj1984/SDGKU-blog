from django.views.generic import ListView, DetailView  
from django.views.generic.edit import CreateView 
from .models import Post

# Create your views here.
class PostListView(ListView):
    template_name = "posts/list.html"
    model = Post

class PostDetailView(DetailView):
    template_name = "posts/detail.html"
    model = Post

class PostCreateView(CreateView):
    template_name = "posts/create.html"
    model = Post
    fields = ['title', 'subtitle', 'body']

    