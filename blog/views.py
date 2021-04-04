from django.shortcuts import render, get_object_or_404
from .models import Blog


def home(request):
    return render(request, 'blog/home.html')


def show_blog(request, blog_id):
    blog = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'blog/show_blog.html', {'blog': blog})