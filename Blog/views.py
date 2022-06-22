from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Post

# def home(request):
# 	return render(request, 'base.html', {})

class HomeView(ListView):
	model = Post
	template_name = 'base.html'
