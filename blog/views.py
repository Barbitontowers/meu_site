from django.shortcuts import render
from django.views.generic import DetailView, ListView
from django.views.generic.edit import CreateView
from .models import Post


class PostListView(ListView):
    model = Post
    template_name = 'post/home.html' 


class PostDetailView(DetailView):
    model = Post
  #  template_name = 'post/detail.html'

class PostCreatelView(CreateView):
    model = Post
#    template_name = 'post/post_new.html'
#    fields = '__all__'


