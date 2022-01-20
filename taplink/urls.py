from django.urls import path
from .views import links_list

from django.conf.urls.static import static
from django.conf import settings

appname = "taplink"

urlpatterns = [
    path('', links_list, name='links_list_url'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
