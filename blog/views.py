from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def blog(request):
    return render(request, 'blog/blog.html')


def posts(request):
    return HttpResponse("This is the blog post")
