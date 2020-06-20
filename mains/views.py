from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'mains/index.html')


def menu(request):
    return render(request, 'mains/menu.html')


def rank(request):
    return render(request, 'mains/rank.html')
