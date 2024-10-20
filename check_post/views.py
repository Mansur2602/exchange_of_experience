from django.shortcuts import render

# Create your views here.

def check_post(request):
    return render(request, 'check_post/check_post.html')