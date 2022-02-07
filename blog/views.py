from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse


# Create your views here.

def starting_page(request):
    return render(request, "blog/index.html")


def posts(request):
    return HttpResponse("HIIIIIIIIIIIIIIIIIIIIIIIIIIII")


def posts_detail(request):
    pass
