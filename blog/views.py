from django.shortcuts import render
from .models import *
from .utils import ObjectDetailMixin
from django.views.generic import View

def estates_list(request):
    estates = Post.objects.all()
    return render(request, 'blog/posts_list.html', context={'posts': posts})

class EstateDetail(ObjectDetailMixin, View):
    model = Post
    template = 'blog/post_detail.html'
