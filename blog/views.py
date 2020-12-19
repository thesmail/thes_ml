from django.shortcuts import render
from .models import *
from .utils import ObjectDetailMixin
from django.views.generic import View

def posts_list(request):
    posts = Post.objects.all()
    return render(request, 'blog/posts_list.html', context={'posts': posts})

class PostDetail(ObjectDetailMixin, View):
    model = Post
    template = 'blog/post_detail.html'
