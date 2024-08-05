from typing import Any
from django.http import Http404, HttpRequest
from django.shortcuts import render

from blog.data import postss
# Create your views here.


def blog(request):
    context = {'name': 'blog context', 'title': 'Blog', 'posts': postss}
    return render(request, 'blog/index.html', context)


def posts(request):
    context = {'name': ' posts', 'posts': postss}
    return render(request, 'blog/index.html', context)


def post(request: HttpRequest, post_id: int):

    found_post: dict[str, Any] | None = None

    for post in postss:
        if post['id'] == post_id:
            found_post = post
            break

    if found_post is None:
        raise Http404('Post not found')

    context = {'name': 'post', 'post':
               found_post, 'title': found_post['title']}
    return render(request, 'blog/post.html', context)
