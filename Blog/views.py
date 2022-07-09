from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post
from .Forms import PostForm
from django.urls import reverse_lazy

# def home(request):
# 	return render(request, 'base.html', {'sdh':23})

class MyPosts(ListView):
	model = Post
	template_name = 'my_posts.html'
	# ordering: ['-post_date']

class HomeView(ListView):
	model = Post
	template_name = 'home.html'
	ordering = ['-post_date']

class DetailedView(DetailView):
	model = Post
	template_name = 'article.html'

class AddPostView(CreateView):
	model = Post
	template_name = 'add_post.html'
	form_class = PostForm
	# fields = '__all__'

class EditView(UpdateView):
	model = Post
	template_name = 'update.html'
	form_class = PostForm

class DeleteView(DeleteView):
	model = Post
	template_name = 'home.html'
	success_url = reverse_lazy('home')

class MyPosts(ListView):
	model = Post
	template_name = 'my_posts.html'
	ordering: ['-post_date']


