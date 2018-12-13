from django.shortcuts import render

# Create your views here.
def index(request):

    return render(request,'home_page.html')


def haha(request):
    return render(request,'haha.html')


def register(request):
    return render(request,'register.html')