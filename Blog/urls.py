from django.urls import path
from . import views

urlpatterns = [
	# path('', views.home, name='home')
	path('', views.HomeView.as_view(), name='home'),
	path('Article/<int:pk>', views.DetailedView.as_view(), name='article'),
	path('Add_Post/', views.AddPostView.as_view(), name='add_post'),
]