from django.contrib import admin

from .models import Link, Social, TapLinkConfiguration
from solo.admin import SingletonModelAdmin

admin.site.register(TapLinkConfiguration, SingletonModelAdmin)
admin.site.register(Link)
admin.site.register(Social)