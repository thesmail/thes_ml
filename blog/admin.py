from django.contrib import admin

from .models import Post

from django_summernote.admin import SummernoteModelAdmin
# from .models import SomeModel

class SomeModelAdmin(SummernoteModelAdmin):  # instead of ModelAdmin
    summernote_fields = 'body'

admin.site.register(Post, SomeModelAdmin)