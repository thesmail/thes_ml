from django.urls import path
from .views import *

from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', posts_list, name='posts_list_url'),
    # path('post/create/', PostCreate.as_view(), name='post_create_url'),
    path('<str:slug>/', PostDetail.as_view(), name='post_detail_url')
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
