from django.contrib import admin
from django.urls import path
from profiles.views import profile_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', profile_view, name = 'profiles')
]
