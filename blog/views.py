from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import View
from django.core.paginator import Paginator


from .models import *
from taplink.models import Social
from .utils import ObjectDetailMixin, ObjectCreateMixin
# from .forms import PostForm

def get_social():
    social = Social.objects.all()
    return social

def error_404(request, exception):
    return render(request, 'blog/error/404.html')

def posts_list(request):
    posts = Post.objects.filter(nav_status=False, status='published')
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
        'socials': get_social(),
        'nav_bar': Post.objects.filter(nav_status=True)
    }

    return render(request, 'blog/posts_list.html', context=context)

def post_detail(request, slug):
    post = get_object_or_404(Post.objects.filter(status='published'), slug__iexact=slug)

    context = {
        'post': post,
        'post_bar': Post.objects.filter(nav_status=True),
        'socials': get_social()
    }

    return render(request, 'blog/post_detail.html', context=context)

# class PostCreate(ObjectCreateMixin, View):
#     form_model = PostForm
#     template = 'blog/post_create_form.html'