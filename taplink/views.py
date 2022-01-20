from django.shortcuts import render

from .models import Link, Social

def links_list(request):
    links = Link.objects.all()
    socials = Social.objects.all()

    context = {
        'links': links,
        'socials': socials
    }

    return render(request, 'taplink/links_list.html', context=context)