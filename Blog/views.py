from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post, category
from .Forms import PostForm
from django.urls import reverse_lazy, reverse
from django.http import HttpResponseRedirect

# def home(request):
# 	return render(request, 'base.html', {'sdh':23})

def like_post(request, pk):
	post = get_object_or_404(Post, id=request.POST.get('post_id'))
	post.likes.add(request.user)

	return HttpResponseRedirect(reverse('article', args=[str(pk)]))

def Category(request, cat):
	category_posts = Post.objects.filter(category= cat)
	cat_menu = category.objects.all()
	return render(request, 'category.html', {'category_posts':category_posts, 'cat':cat, 'cat_menu': cat_menu})

class MyPosts(ListView):
	model = Post
	template_name = 'my_posts.html'
	# ordering: ['-post_date']

class HomeView(ListView):
	model = Post
	template_name = 'home.html'
	ordering = ['-post_date']

	def get_context_data(self, *args, **kwargs):
		cat_menu = category.objects.all()
		context = super(HomeView, self).get_context_data(*args,**kwargs)
		context['cat_menu'] = cat_menu
		return context

class DetailedView(DetailView):
	model = Post
	template_name = 'article.html'

	def get_context_data(self, *args, **kwargs):
		cat_menu = category.objects.all()
		context = super(DetailedView, self).get_context_data(*args,**kwargs)
		context['cat_menu'] = cat_menu
		post = 	get_object_or_404(Post, id=self.kwargs['pk'])
		total_likes = post.total_likes()
		context['total_likes'] = total_likes
		return context


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



