from django.contrib import admin
from django.urls import path
from check_post.views import check_post

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', check_post, name = 'check_post')
]