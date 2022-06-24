from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from .models import Post
from .Forms import PostForm

# def home(request):
# 	return render(request, 'base.html', {'sdh':23})

class HomeView(ListView):
	model = Post
	template_name = 'home.html'

class DetailedView(DetailView):
	model = Post
	template_name = 'article.html'

class AddPostView(CreateView):
	model = Post
	template_name = 'add_post.html'
	form_class = PostForm
	# fields = '__all__'
