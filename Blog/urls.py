from django.urls import path
from . import views

urlpatterns = [
	# path('', views.home, name='home')
	path('', views.HomeView.as_view(), name='home'),
	path('Article/<int:pk>', views.DetailedView.as_view(), name='article'),
	path('Add_Post/', views.AddPostView.as_view(), name='add_post'),
	path('Article/<int:pk>/edit', views.EditView.as_view(), name='edit'),
	path('Article/<int:pk>/delete', views.DeleteView.as_view(), name='delete'),
	path('<str:user>/MyPosts', views.MyPosts.as_view(), name='my_posts'),
	path('like_post/<int:pk>', views.like_post, name='like_post'),
	path('Category/<str:cat>', views.Category, name='category'),
]