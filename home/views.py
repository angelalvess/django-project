from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def home(request):

    context = {'name': 'Rahuls', 'title': 'Home'}
    return render(request, 'home/index.html', context)


def abc(request):
    return HttpResponse("This is the abc page")
