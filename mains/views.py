from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'mains/index.html')


def menu(request):
    return render(request, 'mains/menu.html')


def rank(request):
    return render(request, 'mains/rank.html')


def content(request):
    return render(request, 'mains/content.html')


def insite(request):
    return render(request, 'mains/insite.html')


# def content1(request):
#     return render(request, 'mains/content1.html')