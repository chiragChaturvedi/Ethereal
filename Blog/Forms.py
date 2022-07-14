from random import choices
from django import forms
from .models import Post, category

choices = category.objects.all().values_list('name', 'name')
choices_list = [item for item in choices]    
# choices = [('coding', 'coding'), ('general', 'general'), ('DSA', 'DSA'),]

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'body', 'author', 'category', 'likes', 'snippet')

        widgets = {
            'title' : forms.TextInput(attrs={'class': 'form-control'}),
            'body' : forms.Textarea(attrs={'class': 'form-control'}),
            'author' : forms.TextInput(attrs={'class': 'form-control', 'value':'', 'id':'id_author', "type":"hidden"}),	
            'category' : forms.Select(choices=choices_list ,attrs={'class': 'form-control'}),
            'snippet' : forms.Textarea(attrs={'class': 'form-control'}),
        }
    
