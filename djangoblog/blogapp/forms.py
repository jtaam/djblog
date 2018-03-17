from django import forms
from .models import article

class createForm(forms.ModelForm):
    class Meta:
        model = article
        fields = [
            'article_author',
            'title',
            'body',
            'image',
            'category'
        ]