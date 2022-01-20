from django.contrib import admin
from .models import Post, BlogConfiguration

from django_summernote.admin import SummernoteModelAdmin
from solo.admin import SingletonModelAdmin


class SomeModelAdmin(SummernoteModelAdmin):  # instead of ModelAdmin
    summernote_fields = 'body'

admin.site.register(Post, SomeModelAdmin)
admin.site.register(BlogConfiguration, SingletonModelAdmin)