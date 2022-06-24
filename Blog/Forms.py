from socket import fromshare
from django import forms
from matplotlib import widgets
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'body', 'author')

        widgets = {
            'Title' : forms.TextInput(attrs={'class': 'form-control'}),
            'Author' : forms.Select(attrs={'class': 'form-control'}),
            'Body' : forms.Textarea(attrs={'class': 'form-control'}),

        }