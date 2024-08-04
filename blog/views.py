from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def blog(request):
    context = {'name': 'blog context', 'title': 'Blog'}
    return render(request, 'blog/index.html', context)


def posts(request):
    context = {'name': 'blog posts'}
    return HttpResponse("This is the blog post", context)
