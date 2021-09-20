from django import forms
from .models import *

from django.core.exceptions import ValidationError
from django_summernote.widgets import SummernoteWidget, SummernoteInplaceWidget

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ['title', 'quo', 'body', 'img']

        widgets = {
            'body': SummernoteWidget(),
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'quo': forms.TextInput(attrs={'class': 'form-control'}),
            'img': forms.FileInput(attrs={'class': 'form-control'})
        }
    def clean_slug(self):
        new_slug = self.cleaned_data['slug'].lower()

        if new_slug == 'create':
            raise ValidationError('Slug may not be "Create"')
        return new_slug