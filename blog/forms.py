from django import forms
from .models import *

from django.core.exceptions import ValidationError
from pagedown.widgets import PagedownWidget

class PostForm(forms.ModelForm):
    body = forms.CharField(widget=PagedownWidget())

    class Meta:
        model = Post
        fields = ['title', 'img', 'body']

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            # 'img': forms.ImageField(),
            # 'body': forms.Textarea(attrs={'class': 'form-control'}),
        }
    def clean_slug(self):
        new_slug = self.cleaned_data['slug'].lower()

        if new_slug == 'create':
            raise ValidationError('Slug may not be "Create"')
        return new_slug