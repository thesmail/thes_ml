from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('golem/', admin.site.urls),
    path('', include('blog.urls')),
    path('', include('pagedown.urls')),
    path('summernote/', include('django_summernote.urls')),
]

handler404 = 'blog.views.error_404'