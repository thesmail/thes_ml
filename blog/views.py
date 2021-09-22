from django.shortcuts import render, redirect
from django.views.generic import View
from django.core.paginator import Paginator


from .models import *
from .utils import ObjectDetailMixin, ObjectCreateMixin
from .forms import PostForm

def error_404(request, exception):
    return render(request, 'error/404.html')

def posts_list(request):
    posts = Post.objects.filter(nav_status=False)
    paginator = Paginator(posts, 5)

    page_number = request.GET.get('page', 1)
    page = paginator.get_page(page_number)

    is_paginated = page.has_other_pages()

    if page.has_previous():
        prev_url = '?page={}'.format(page.previous_page_number())
    else:
        prev_url = ''

    if page.has_next():
        next_url = '?page={}'.format(page.next_page_number())
    else:
        next_url = ''

    context = {
        'page_object': page,
        'is_paginated': is_paginated,
        'next_url': next_url,
        'prev_url': prev_url,
        'post_bar': Post.objects.filter(nav_status=True)
    }

    return render(request, 'blog/posts_list.html', context=context)

class PostDetail(ObjectDetailMixin, View):
    model = Post
    template = 'blog/post_detail.html'

class PostCreate(ObjectCreateMixin, View):
    form_model = PostForm
    template = 'blog/post_create_form.html'