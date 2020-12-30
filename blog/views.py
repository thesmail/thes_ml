from django.shortcuts import render, redirect
from django.views.generic import View

from .models import *
from .utils import ObjectDetailMixin, ObjectCreateMixin
from .forms import PostForm

def posts_list(request):
    posts = Post.objects.all()
    return render(request, 'blog/posts_list.html', context={'posts': posts})

class PostDetail(ObjectDetailMixin, View):
    model = Post
    template = 'blog/post_detail.html'

class PostCreate(ObjectCreateMixin, View):
    form_model = PostForm
    template = 'blog/post_create_form.html'