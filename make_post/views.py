from django.shortcuts import render

# Create your views here.

def make_posts(request):
    return render(request, 'make_post/make_post.html')