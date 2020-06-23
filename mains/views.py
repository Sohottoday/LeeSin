from django.shortcuts import render
from .pro_crawling import main_crawling

# Create your views here.
def index(request):
    main_crawling.crawling()
    return render(request, 'mains/index.html')


def menu(request):
    return render(request, 'mains/menu.html')


def rank(request):
    return render(request, 'mains/rank.html')


def content(request):
    return render(request, 'mains/content.html')


def content1(request):
    return render(request, 'mains/content1.html')