from django.contrib import admin
from django.urls import path
from make_post.views import make_posts

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', make_posts, name = 'make_post')
]