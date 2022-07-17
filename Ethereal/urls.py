from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('Home.urls')),
    path('', include('Blog.urls')),
    path('Members/', include('django.contrib.auth.urls')),
    path('Members/', include('Members.urls')),
]
